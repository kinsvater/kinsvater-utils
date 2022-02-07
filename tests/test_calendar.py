import datetime

from kinsvater_utils.calendar import CalendarReader


class TestCalendarReader:

    def test_get_holidays(self):
        start_date = datetime.date(2019, 5, 12)
        end_date = datetime.date(2021, 3, 4)
        country_code = 'FR'

        cal = CalendarReader(start_date=start_date, end_date=end_date,
                             country_code=country_code)

        holidays = cal.get_holidays()

        assert datetime.date(2019, 11, 1) in holidays
        assert start_date <= min(holidays) <= max(holidays) <= end_date
