import datetime as dt
import dateutil.relativedelta as rd

from typing import Dict, List, Tuple
from docutils.nodes import Node, system_message, inline
from docutils.parsers.rst.states import Inliner
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxRole
import re

_date_re = re.compile(r'wk(?P<week>\d+)\s+(?P<weekday>\w+)(?:\s+(?P<keyword>\w+))?')

_weekdays = {
    'sun': rd.SU,
    'mon': rd.MO,
    'tue': rd.TU,
    'wed': rd.WE,
    'thu': rd.TH,
    'fri': rd.FR,
    'sat': rd.SA,
}


class DateRole(SphinxRole):
    @property
    def course_start(self):
        return self.config.course_start

    def __call__(self, name: str, rawtext: str, text: str, lineno: int,
                 inliner: Inliner, options: Dict = {}, content: List[str] = []
                 ) -> Tuple[List[Node], List[system_message]]:
        self.inliner = inliner

        match = _date_re.match(text)
        self.keyword = match.group('keyword')
        if match:
            week = int(match.group('week'))
            if week >= self.config.break_week:
                week += 1
            weekday = match.group('weekday')
            weekday = _weekdays[weekday]
            self.delta = rd.relativedelta(weekday=weekday(week))
        else:
            raise ValueError('unknown date ' + text)

        return super().__call__(name, rawtext, text, lineno, inliner, options, content)

    def run(self):
        date = self.course_start + self.delta
        if self.keyword == 'long':
            ds = date.strftime('%B %#d')
        else:
            ds = date.strftime('%#m/%#d')

        dn = inline('', ds)
        return [dn], []


def setup(app: Sphinx):
    app.add_config_value('course_start', None, 'html')
    app.add_config_value('break_week', 14, 'html')
    app.add_role('date', DateRole())
