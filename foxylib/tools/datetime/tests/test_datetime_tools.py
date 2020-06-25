import logging
from datetime import datetime, timedelta, time
from datetime import datetime
from unittest import TestCase

import pytz

from foxylib.tools.datetime.datetime_tool import DatetimeTool, DatetimeUnit, TimedeltaTool, TimeTool, Nearest
from foxylib.tools.log.foxylib_logger import FoxylibLogger


class DatetimeToolTest(TestCase):
    @classmethod
    def setUpClass(cls):
        FoxylibLogger.attach_stderr2loggers(logging.DEBUG)

    def test_01(self):
        tz_la = pytz.timezone("America/Los_Angeles")

        dt_from = datetime(2020, 1, 1, tzinfo=tz_la)
        dt_to = datetime(2020, 1, 2, tzinfo=tz_la)

        hyp = DatetimeTool.datetime_pair2days_difference((dt_from, dt_to,))
        self.assertEqual(hyp, 1)


    # daylight saving start
    def test_02(self):

        tz_la = pytz.timezone("America/Los_Angeles")

        dt_from = datetime(2020, 3, 7, tzinfo=tz_la)
        dt_to = datetime(2020, 3, 9, tzinfo=tz_la)

        hyp = DatetimeTool.datetime_pair2days_difference((dt_from, dt_to,))
        self.assertEqual(hyp, 2)

    # daylight saving end
    def test_03(self):
        tz_la = pytz.timezone("America/Los_Angeles")

        dt_from = datetime(2020, 10, 31, tzinfo=tz_la)
        dt_to = datetime(2020, 11, 2, tzinfo=tz_la)

        hyp = DatetimeTool.datetime_pair2days_difference((dt_from, dt_to,))
        self.assertEqual(hyp, 2)

    def test_04(self):
        dt_pivot = datetime(2022, 2, 2, 22, 22, 22, 222222)

        hyp = DatetimeTool.truncate(dt_pivot, unit=DatetimeUnit.Value.MILLISEC)
        ref = datetime(2022, 2, 2, 22, 22, 22, 222000)
        self.assertEqual(hyp, ref)

    def test_05(self):
        dt_start = datetime(2020, 2, 29, 22, 22, 22, 222222)
        dt_end = datetime(2021, 2, 28, 22, 22, 22, 222222)

        hyp = DatetimeTool.datetime_span2years([dt_start,dt_end])
        ref = 0
        self.assertEqual(hyp, ref)

    def test_06(self):
        dt_start = datetime(2020, 2, 28, 22, 22, 22, 222222)
        dt_end = datetime(2021, 2, 28, 22, 22, 22, 222222)

        hyp = DatetimeTool.datetime_span2years([dt_start,dt_end])
        ref = 1
        self.assertEqual(hyp, ref)

    def test_07(self):
        td = timedelta(days=7, seconds=4*60*60+7*60+5, microseconds=2312)

        unit_day = TimedeltaTool.unit_day()
        unit_hour = TimedeltaTool.unit_hour()
        unit_minute = TimedeltaTool.unit_minute()
        unit_second = TimedeltaTool.unit_second()

        self.assertEqual(TimedeltaTool.timedelta_unit_pair2quotient(td, unit_hour, unit_day), 4)
        self.assertEqual(TimedeltaTool.timedelta_unit_pair2quotient(td, unit_minute, unit_hour), 7)
        self.assertEqual(TimedeltaTool.timedelta_unit_pair2quotient(td, unit_second, unit_minute), 5)


class TestTimeTool(TestCase):
    def test_01(self):
        logger = FoxylibLogger.func_level2logger(self.test_01, logging.DEBUG)

        tz = pytz.timezone("America/Los_Angeles")
        dt_tz = datetime.now(tz=tz)

        hours_1 = timedelta(seconds=60 * 60)
        hours_23 = timedelta(seconds=60 * 60 * 23)
        hours_24 = timedelta(seconds=60 * 60 * 24)
        # hours_25 = timedelta(seconds=60 * 60 * 25)

        time_past = (dt_tz - timedelta(seconds=60 * 5)).timetz()
        dt_coming_of_past = TimeTool.time2datetime_nearest(time_past, dt_tz, timedelta(days=1), Nearest.COMING)

        self.assertGreater(dt_coming_of_past, dt_tz + hours_23)
        self.assertLess(dt_coming_of_past, dt_tz + hours_24)

        time_future = (dt_tz + timedelta(seconds=60 * 5)).timetz()

        dt_coming_of_future = TimeTool.time2datetime_nearest(time_future, dt_tz, timedelta(days=1), Nearest.COMING)

        self.assertGreater(dt_coming_of_future, dt_tz)
        # raise Exception({"dt_tz + hours_24": dt_tz + hours_24,
        #                  "dt_future_of_future": dt_future_of_future,
        #                  })

        self.assertLess(dt_coming_of_future, dt_tz + hours_1)

    def test_02(self):
        dt_now = datetime.now(pytz.utc)
        dt_from = dt_now - timedelta(seconds=60)
        dt_result = DatetimeTool.from_pivot_period2next(dt_from, dt_now, timedelta(days=1))

        self.assertEqual(dt_result, dt_from + timedelta(days=1))

