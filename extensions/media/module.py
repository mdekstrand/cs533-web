"""
Sphinx extension to implement video support
"""

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective
from sphinx.transforms import SphinxTransform


class ModuleDirective(SphinxDirective):
    required_arguments = 1
    optional_arguments = 0
    has_content = False
    option_spec = {
        'playlist': directives.path,
        'folder': directives.path,
    }

    def run(self):
        name = self.arguments[0].strip()
        self.env.ref_context['res:module'] = name
        pending = nodes.pending(ModTocTransform, {
            'module': name,
            'playlist': self.options.get('playlist')
        })

        top = self.state.document.children[0]
        top['ids'].append(name)
        title = top.children[0].astext()

        dom = self.env.get_domain('res')
        dom.note_module(name, title)

        self.state.document.note_pending(pending, 500)
        return [pending]


class ModTocTransform(SphinxTransform):
    def apply(self, **kwargs):
        mod = self.startnode.details['module']
        box = nodes.container('', is_div=True, classes=['module-content'])

        table = nodes.table(classes=['colwidths-auto'])
        tg = nodes.tgroup(cols=2)
        tg += nodes.colspec(colwidth=1)
        tg += nodes.colspec(colwidth=0)
        table += tg
        head = nodes.thead()
        hrow = nodes.row()
        head += hrow
        hrow += nodes.entry('', nodes.strong('', 'Element'))
        hrow += nodes.entry('', nodes.strong('', 'Length'))
        tg += head

        tb = nodes.tbody()
        tg += tb

        tot_vid = 0.0
        tot_words = 0

        for obj in self.env.domaindata['res']['objects']:
            if obj.module != mod:
                continue

            if hasattr(obj, 'vid_length'):
                vl = obj.vid_length()
                if vl:
                    tot_vid += vl

            if hasattr(obj, 'read_length'):
                rl = obj.read_length()
                if rl:
                    tot_words += rl

            row = nodes.row()

            l_cell = nodes.entry()
            ref = nodes.reference('', '', internal=True)
            ref['refid'] = obj.anchor
            ref += nodes.inline('', obj.display_title)
            l_cell += nodes.paragraph('', '', ref)
            row += l_cell

            len_cell = nodes.entry()
            if hasattr(obj, 'length'):
                len_cell += nodes.inline('', obj.length)
            row += len_cell
            tb += row

        box += table

        summary = nodes.paragraph()
        summary += nodes.inline('', 'This week has ')
        summary += nodes.strong('', '%dh%.0fm' % (int(tot_vid / 3600), tot_vid % 3600 / 60))
        summary += nodes.inline('', ' of video and ')
        summary += nodes.strong('', '%d words' % (tot_words,))
        summary += nodes.inline('', ' of assigned readings.')

        folder = self.startnode.details.get('folder', None)
        playlist = self.startnode.details.get('playlist', None)

        if playlist:
            summary += nodes.inline('', " This week's videos are available as a ")
            plref = nodes.reference('', '', classes=['panopto'])
            plref['refuri'] = playlist
            plref += nodes.inline('', 'Panopto playlist')
            summary += plref
            summary += nodes.inline('', ".")
        elif folder:
            summary += nodes.inline('', " This week's videos are available in a ")
            plref = nodes.reference('', '', classes=['panopto'])
            plref['refuri'] = f'https://boisestate.hosted.panopto.com/Panopto/Pages/Sessions/List.aspx#folderID=%22{folder}%22'
            plref += nodes.inline('', 'Panopto folder')
            summary += plref
            summary += nodes.inline('', ".")

        box += summary

        parent = self.startnode.parent
        parent.replace(self.startnode, box)
