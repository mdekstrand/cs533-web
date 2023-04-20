import * as toml from "std/toml/mod.ts";
import { deepMerge } from "std/collections/deep_merge.ts";
import { basename } from "std/path/mod.ts";
import docopt from "docopt";

const doc = `
List BunnyCDN videos.

Usage:
  video-upload.js [options] --list
  video-upload.js [options] --upload [--delete] FILE...

Options:
  -o FILE
    Write output to FILE.
  --list
    List the videos.
`;

async function loadSettings() {
    let text = await Deno.readTextFile('media.toml');
    let settings = toml.parse(text);

    try {
        text = await Deno.readTextFile('media.local.toml');
        settings = deepMerge(settings, toml.parse(text));
    } catch (e) {
        if (e instanceof Deno.errors.NotFound) {
            console.warn('media.local.toml not found');
        } else {
            console.error('error reading media.local.toml:% s', e);
            throw e;
        }
    }

    return settings;
}

async function invokeAPI(method, path, body) {
  const base = new URL(`https://video.bunnycdn.com/library/${settings.videos.library_id}/`)
  const url = new URL(path, base);
  const headers = {
    AccessKey: settings.videos.access_key,
  };
  if (body && typeof(body) == 'object') {
    headers['content-type'] = 'application/json';
    body = JSON.stringify(body);
  }

  console.debug('%s %s', method, path);
  const res = await fetch(url, {
    method,
    headers,
    body,
  });
  if (!res.ok) {
    console.error('%s %s: failed with code %d', method, path, res.status);
    throw new Error(`HTTP ${res.status}`);
  }
  return await res.json();
}

async function fetchVideoList() {
  const manifest = await invokeAPI('GET', 'videos?itemsPerPage=1000&orderBy=title');
  console.log('have %d videos', manifest.totalItems);
  return manifest;
}

async function listVideos() {
  const manifest = await fetchVideoList();
  const outfn = options['-o'];
  if (outfn) {
    console.info('saving to %s', outfn);
    await Deno.writeTextFile(outfn, JSON.stringify(manifest));
  }
  for (const video of manifest.items) {
    console.info('video %s (%s): %f', video.title, video.guid, video.length);
    if (video.hasMP4Fallback) {
      console.warn('  %cMP4 fallback detected', 'color: red');
    }
  }
}

async function uploadVideos(files) {
  const manifest = await fetchVideoList();
  const videos = {};
  for (const vid of manifest.items) {
    videos[vid.title] = vid;
  }
  for (const file of files) {
    const name = basename(file);
    let vid = videos[name];
    let collectionId;
    if (vid) {
      collectionId = vid.collectionId;
      if (options['--delete']) {
        console.info('video %s exists, deleting', vid.guid);
        await invokeAPI('DELETE', `videos/${vid.guid}`);
      } else {
        console.warn('video %s already exists, but not deleting');
      }
    }

    console.info('video creating video %s', name);
    vid = await invokeAPI('POST', 'videos', {title: name, collectionId});
    console.info('uploading %s to %s', file, vid.guid);
    const stream = await Deno.open(file, {read: true});
    try {
      await invokeAPI('PUT', `videos/${vid.guid}`, stream);
      console.info('upload completed');
    } finally {
      await stream.close();
    }
  }
}

const settings = await loadSettings();
const options = docopt(doc);

if (options['--list']) {
  await listVideos();
} else if (options['--upload']) {
  await uploadVideos(options['FILE']);
}
