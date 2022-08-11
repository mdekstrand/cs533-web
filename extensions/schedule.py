import arrow

from functools import total_ordering
from typing import Dict, List, Tuple
from docutils.nodes import Node, system_message, inline, Text, admonition, title
from docutils.parsers.rst.states import Inliner
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxRole, SphinxDirective
import re

_date_re = re.compile(r'w(?:ee)?k(?P<week>\d+)\s+(?P<weekday>\w+)(?:\s+(?P<keyword>\w+))?')

_weekdays = {
    'sun': 6,
    'mon': 0,
    'tue': 1,
    'wed': 2,
    'thu': 3,
    'fri': 4,
    'sat': 5,
}


@total_ordering
class Term:
    def __init__(self, term_string):
        self.term_string = term_string

    @property
    def year(self):
        y = int(self.term_string[1:])
        return 2000 + y

    @property
    def term_code(self):
        return self.term_string[0]

    @property
    def term_name(self):
        match self.term_code:
            case 'F': return 'Fall'
            case 'S': return 'Spring'
            case _: raise ValueError('unknown term {}'.format(self.term_code))

    @classmethod
    def _is_valid_operand(cls, other):
        return hasattr(other, 'term_string')

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented

        return self.term_string == other.term_string

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented

        if self.term_string == other.term_string:
            return False
        elif self.year < other.year:
            return True
        elif self.year == other.year:
            match (self.term_code, other.term_code):
                case ('S', 'F'): return True
                case ('F', 'S'): return False
                case _: raise ValueError('unexpected term codes')
        else:
            return False


class DateRole(SphinxRole):
    @property
    def course_start(self):
        return arrow.get(self.config.course_start)

    def __call__(self, name: str, rawtext: str, text: str, lineno: int,
                 inliner: Inliner, options: Dict = {}, content: List[str] = []
                 ) -> Tuple[List[Node], List[system_message]]:
        self.inliner = inliner

        match = _date_re.match(text)
        self.keyword = match.group('keyword')
        date = self.course_start
        if match:
            week = int(match.group('week'))
            if week >= self.config.break_week:
                week += 1

            wstart = date.shift(weeks=(week - 1))
            weekday = match.group('weekday')

            if weekday == 'range':
                self.date = (wstart, wstart.shift(weekday=4))
            else:
                weekday = _weekdays[weekday]
                self.date = wstart.shift(weekday=weekday)
        else:
            raise ValueError('unknown date ' + text)

        return super().__call__(name, rawtext, text, lineno, inliner, options, content)

    def run(self):
        if isinstance(self.date, tuple):
            start, end = self.date

            ds1 = start.format('M/D')
            if start.month == end.month:
                ds2 = end.format('D')
            else:
                ds2 = end.format('M/D')
            ds = f'{ds1}–{ds2}'

        else:
            if self.keyword == 'xlong':
                fmt = 'dddd, MMMM D, YYYY'
            elif self.keyword == 'long':
                fmt = 'MMMM D'
            else:
                fmt = 'M/D'

            ds = self.date.format(fmt)

        # dn = inline('', ds)
        dn = Text(ds)
        return [dn], []


class UpdateBannerDirective(SphinxDirective):
    required_arguments = 1
    optional_arguments = 0
    has_content = True

    @property
    def current_term(self):
        return Term(self.config.term)

    def run(self):
        update_term = self.arguments[0].strip()
        update_term = Term(update_term)

        if update_term >= self.current_term:
            return []  # nothing to do, we are up to date!

        for node in self.state.document.traverse(title):
            node.children.insert(0, inline('', '🚧 '))
            node.children.append(inline('', ' 🚧'))

        if self.content:
            content = self.content
        else:
            content = ["""
This page has not yet been updated for the current term.  It is here for your reference,
but do not treat it as final until this admonition has been removed.  Content may change
significantly, videos may be replaced, etc.  This page was last updated
for the **{term_name} {term_year}** term.
            """.format(term_name=update_term.term_name, term_year=update_term.year).strip()]

        cstr = '\n'.join('content')
        node = admonition(cstr, classes=['warning', 'update'])

        tn = title('', '', inline('', 'Page Not Final — Under Review'))
        node += tn
        self.state.nested_parse(content, self.content_offset, node)

        return [node]


def setup(app: Sphinx):
    app.add_config_value('term', None, 'html')
    app.add_config_value('course_start', None, 'html')
    app.add_config_value('break_week', 14, 'html')
    app.add_role('date', DateRole())
    app.add_directive('updated', UpdateBannerDirective)

    return {
        'version': 1,
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }
