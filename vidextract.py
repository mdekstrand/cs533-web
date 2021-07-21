"""
Extract video data.

Usage:
    vidextract.py FILE
"""

from pathlib import Path
import xml.etree.ElementTree as ET
from datetime import timedelta
from docopt import docopt

class NSPrefixer:
    def __init__(self, ns):
        self.ns_uri = ns
    
    def __getattr__(self, name):
        return '{%s}%s' % (self.ns_uri, name)

xmlns = {
    'xmpDM': 'http://ns.adobe.com/xmp/1.0/DynamicMedia/',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
}

xmpDM = NSPrefixer(xmlns['xmpDM'])

def extract_toc(src, dst):
    et = ET.parse(src)
    dur_node = et.find('.//xmpDM:duration', namespaces=xmlns)
    dur = dur_node.get(xmpDM.value)
    dur = int(dur)

    nodes = et.findall(".//*[@xmpDM:trackType='TableOfContents']//rdf:Description", namespaces=xmlns)
    # nodes = et.findall(".//*[@xmpDM:trackName='TableOfContents']//rdf:Description")
    toc = [(int(n.get(xmpDM.startTime)), n.get(xmpDM.name)) for n in nodes]
    ends = [st for (st,n) in toc[1:]] + [dur]

    with open(dst, 'w') as of:
        print('WEBVTT', file=of)
        for (start, name), end in zip(toc, ends):
            s = timedelta(milliseconds=start)
            e = timedelta(milliseconds=end)
            print(s, '-->', e, file=of)
            print(name, file=of)
            print('', file=of)


def main(opts):
    video = opts['FILE']
    video = Path(video)
    out = video.with_name(video.name.replace('_config.xml', '.toc.vtt'))
    extract_toc(video, out)


if __name__ == "__main__":
    opts = docopt(__doc__)
    main(opts)
