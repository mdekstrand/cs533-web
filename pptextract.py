"""
Extract PowerPoint to text.

Based on https://stackoverflow.com/a/47272482/1385039
"""
from os import write
import sys
from pathlib import Path
import csv

from tinytag import TinyTag
import pptx

src_dir = Path(sys.argv[1])
out_dir = Path('pages/videos')

print('loading from', src_dir)

slide_counts = {}
vid_lengths = {}

print('loading slide decks')
for file in src_dir.glob('*.pptx'):
    print('reading', file.name)
    name = file.stem
    out_file = out_dir / f'{name}.txt'
    ppt = pptx.Presentation(file)
    with open(out_file, 'w', encoding='utf8') as otf:
        slide_counts[name] = len(ppt.slides)
        for slide in ppt.slides:
            for shape in slide.shapes:
                text = getattr(shape, 'text', None)
                if text:
                    print(text, file=otf)

print('loading videos')
for file in src_dir.glob('*.mp4'):
    print('scanning', file.name)
    vt = TinyTag.get(file)
    vid_lengths[file.stem] = vt.duration

lectures = set(slide_counts.keys()) | set(vid_lengths.keys())

with open('lectures.csv', 'w', newline='') as wf:
    w = csv.writer(wf)
    w.writerow(['name', 'slides', 'length'])
    for n in sorted(lectures):
        row = n, slide_counts.get(n, None), vid_lengths.get(n, None)
        w.writerow(row)
