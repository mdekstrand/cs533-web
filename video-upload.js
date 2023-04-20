import * as toml from "std/toml/mod.ts";
import { deepMerge } from "std/collections/deep_merge.ts";
import docopt from "docopt";

const doc = `
List BunnyCDN videos.

Usage:
  video-upload.js [options] --list

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

async function invokeAPI(method, path) {
  const base = new URL(`https://video.bunnycdn.com/library/${settings.videos.library_id}/`)
  const url = new URL(path, base);
  const res = await fetch(url, {
    method,
    headers: {
      AccessKey: settings.videos.access_key,
    }
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
  }
}

const settings = await loadSettings();
const options = docopt(doc);

if (options['--list']) {
  await listVideos();
}
