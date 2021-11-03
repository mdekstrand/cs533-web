import arrow

from typing import Dict, List, Tuple
from docutils.nodes import Node, system_message, inline, Text
from docutils.parsers.rst.states import Inliner
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxRole
import re

_date_re = re.compile(r'wk(?P<week>\d+)\s+(?P<weekday>\w+)(?:\s+(?P<keyword>\w+))?')

_weekdays = {
    'sun': 6,
    'mon': 0,
    'tue': 1,
    'wed': 2,
    'thu': 3,
    'fri': 4,
    'sat': 5,
}


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

            ds1 = start.format('MMM. D')
            if start.month == end.month:
                ds2 = end.format('D')
            else:
                ds2 = end.format('MMM. D')
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


def setup(app: Sphinx):
    app.add_config_value('course_start', None, 'html')
    app.add_config_value('break_week', 14, 'html')
    app.add_role('date', DateRole())
