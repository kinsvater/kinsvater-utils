import datetime
from typing import List

from workalendar.core import Calendar
from workalendar.registry import registry


class CalendarReader:
    def __init__(self, start_date: datetime.date, end_date: datetime.date, country_code: str):
        """Collect holidays and other non-working days.

        `country_code` must be in two-letter iso format, all capital.
        """
        self._start_date = start_date
        self._end_date = end_date
        self._country_code = country_code

    def get_holidays(self) -> List[datetime.date]:
        calendar = self._get_calendar()

        relevant_years = range(self._start_date.year, self._end_date.year + 1)

        holidays = list()
        for year in relevant_years:
            holidays.extend(calendar.holidays(year))

        return [date for date, name in holidays if self._start_date <= date <= self._end_date]

    def _get_calendar(self) -> Calendar:
        if self._country_code in registry.region_registry.keys():
            cal_class = registry.get(self._country_code)
            return cal_class()
        else:
            raise RuntimeError('Country code \'{}\' is not supported by workalendar!'.format(self._country_code))
