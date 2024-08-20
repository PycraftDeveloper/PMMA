import math as _math

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

class TimeFormatter:
    def __init__(self):
        self.year = 0
        self.month = 0
        self.day = 0
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.microsecond = 0

    def set_from_year(self, year):
        # Convert to total seconds
        total_seconds = year * Constants.DAYS_PER_YEAR * Constants.SECONDS_PER_DAY

        # Years
        years = _math.floor(year)
        remainder_seconds = total_seconds - (years * Constants.DAYS_PER_YEAR * Constants.SECONDS_PER_DAY)

        # Months
        month = remainder_seconds / (Constants.DAYS_PER_MONTH * Constants.SECONDS_PER_DAY)
        months = _math.floor(month)
        remainder_seconds -= months * Constants.DAYS_PER_MONTH * Constants.SECONDS_PER_DAY

        # Days
        day = remainder_seconds / Constants.SECONDS_PER_DAY
        days = _math.floor(day)
        remainder_seconds -= days * Constants.SECONDS_PER_DAY

        # Hours
        hour = remainder_seconds / Constants.SECONDS_PER_HOUR
        hours = _math.floor(hour)
        remainder_seconds -= hours * Constants.SECONDS_PER_HOUR

        # Minutes
        minute = remainder_seconds / Constants.SECONDS_PER_MINUTE
        minutes = _math.floor(minute)
        remainder_seconds -= minutes * Constants.SECONDS_PER_MINUTE

        # Seconds
        seconds = _math.floor(remainder_seconds)
        remainder_seconds -= seconds

        # Microseconds
        microseconds = _math.floor(remainder_seconds * 1e6)

        self.year = years
        self.month = months
        self.day = days
        self.hour = hours
        self.minute = minutes
        self.second = seconds
        self.microsecond = microseconds

    def set_from_month(self, month):
        # Years
        years = _math.floor(month / 12)
        months_remainder = month - years * 12

        # Months
        months = _math.floor(months_remainder)
        day = (months_remainder - months) * Constants.DAYS_PER_MONTH
        days = _math.floor(day)

        # Remainder in seconds
        remainder_seconds = (day - days) * Constants.SECONDS_PER_DAY

        # Hours
        hours = _math.floor(remainder_seconds / Constants.SECONDS_PER_HOUR)
        remainder_seconds -= hours * Constants.SECONDS_PER_HOUR

        # Minutes
        minutes = _math.floor(remainder_seconds / Constants.SECONDS_PER_MINUTE)
        remainder_seconds -= minutes * Constants.SECONDS_PER_MINUTE

        # Seconds
        seconds = _math.floor(remainder_seconds)
        remainder_seconds -= seconds

        # Microseconds
        microseconds = _math.floor(remainder_seconds * 1e6)

        self.years = years
        self.months = months
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.microseconds = microseconds

    def set_from_day(self, day):
        # Years
        years = _math.floor(day / Constants.DAYS_PER_YEAR)
        days_remainder = day - years * Constants.DAYS_PER_YEAR

        # Months
        months = _math.floor(days_remainder / Constants.DAYS_PER_MONTH)
        days_remainder -= months * Constants.DAYS_PER_MONTH

        # Days
        days = _math.floor(days_remainder)

        # Remainder in seconds
        remainder_seconds = (days_remainder - days) * Constants.SECONDS_PER_DAY

        # Hours
        hours = _math.floor(remainder_seconds / Constants.SECONDS_PER_HOUR)
        remainder_seconds -= hours * Constants.SECONDS_PER_HOUR

        # Minutes
        minutes = _math.floor(remainder_seconds / Constants.SECONDS_PER_MINUTE)
        remainder_seconds -= minutes * Constants.SECONDS_PER_MINUTE

        # Seconds
        seconds = _math.floor(remainder_seconds)
        remainder_seconds -= seconds

        # Microseconds
        microseconds = _math.floor(remainder_seconds * 1e6)

        self.years = years
        self.months = months
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.microseconds = microseconds

    def set_from_hour(self, hour):
        # Years
        days_float = hour / Constants.HOURS_PER_DAY
        years = _math.floor(days_float / Constants.DAYS_PER_YEAR)
        days_remainder = days_float - years * Constants.DAYS_PER_YEAR

        # Months
        months = _math.floor(days_remainder / Constants.DAYS_PER_MONTH)
        days_remainder -= months * Constants.DAYS_PER_MONTH

        # Days
        days = _math.floor(days_remainder)
        hours_remainder = (days_remainder - days) * Constants.HOURS_PER_DAY

        # Hours
        hours = _math.floor(hours_remainder)
        minute = (hours_remainder - hours) * Constants.SECONDS_PER_HOUR / Constants.SECONDS_PER_MINUTE

        # Minutes
        minutes = _math.floor(minute)
        remainder_seconds = (minute - minutes) * Constants.SECONDS_PER_MINUTE

        # Seconds
        seconds = _math.floor(remainder_seconds)
        remainder_seconds -= seconds

        # Microseconds
        microseconds = _math.floor(remainder_seconds * 1e6)

        self.years = years
        self.months = months
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.microseconds = microseconds

    def set_from_minute(self, minute):
        # Years
        hours_float = minute / Constants.MINUTES_PER_HOUR
        days_float = hours_float / Constants.HOURS_PER_DAY
        years = _math.floor(days_float / Constants.DAYS_PER_YEAR)
        days_remainder = days_float - years * Constants.DAYS_PER_YEAR

        # Months
        months = _math.floor(days_remainder / Constants.DAYS_PER_MONTH)
        days_remainder -= months * Constants.DAYS_PER_MONTH

        # Days
        days = _math.floor(days_remainder)
        hours_float = (days_remainder - days) * Constants.HOURS_PER_DAY

        # Hours
        hours = _math.floor(hours_float)
        minutes_remainder = (hours_float - hours) * Constants.MINUTES_PER_HOUR

        # Minutes
        minutes = _math.floor(minutes_remainder)
        remainder_seconds = (minutes_remainder - minutes) * Constants.SECONDS_PER_MINUTE

        # Seconds
        seconds = _math.floor(remainder_seconds)
        remainder_seconds -= seconds

        # Microseconds
        microseconds = _math.floor(remainder_seconds * 1e6)

        self.years = years
        self.months = months
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.microseconds = microseconds

    def set_from_second(self, second):
        # Years
        days_float = second / Constants.SECONDS_PER_DAY
        years = _math.floor(days_float / Constants.DAYS_PER_YEAR)
        days_remainder = days_float - years * Constants.DAYS_PER_YEAR

        # Months
        months = _math.floor(days_remainder / Constants.DAYS_PER_MONTH)
        days_remainder -= months * Constants.DAYS_PER_MONTH

        # Days
        days = _math.floor(days_remainder)
        hours_float = (days_remainder - days) * Constants.HOURS_PER_DAY

        # Hours
        hours = _math.floor(hours_float)
        minutes_float = (hours_float - hours) * Constants.MINUTES_PER_HOUR

        # Minutes
        minutes = _math.floor(minutes_float)
        remainder_seconds = (minutes_float - minutes) * Constants.SECONDS_PER_MINUTE

        # Seconds
        seconds = _math.floor(remainder_seconds)
        remainder_seconds -= seconds

        # Microseconds
        microseconds = _math.floor(remainder_seconds * 1e6)

        self.years = years
        self.months = months
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.microseconds = microseconds

    def set_from_microsecond(self, microsecond):
        # Convert microseconds to seconds
        seconds_float = microsecond / Constants.MICROSECONDS_PER_SECOND

        # Use the seconds conversion function
        return self.set_from_second(seconds_float)

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def get_hour(self):
        return self.hour

    def get_minute(self):
        return self.minute

    def get_second(self):
        return self.second

    def get_microsecond(self):
        return self.microsecond

    def get_in_date_format(self):
        return f"{self.day}/{self.month}/{self.year} @ {self.hour}:{self.minute}:{self.second}.{self.microsecond}"

    def get_in_sentence_format(self):
        output_string = ""
        if self.year > 0:
            if self.year > 1:
                output_string += f"{self.year} years, "
            else:
                output_string += f"{self.year} year, "

        if self.month > 0:
            if self.month > 1:
                output_string += f"{self.month} months, "
            else:
                output_string += f"{self.month} month, "

        if self.day > 0:
            if self.day > 1:
                output_string += f"{self.day} days, "
            else:
                output_string += f"{self.day} day, "

        if self.hour > 0:
            if self.hour > 1:
                output_string += f"{self.hour} hours, "
            else:
                output_string += f"{self.hour} hour, "

        if self.minute > 0:
            if self.minute > 1:
                output_string += f"{self.minute} minutes, "
            else:
                output_string += f"{self.minute} minute, "

        if self.second > 0:
            if self.second > 1:
                output_string += f"{self.second} seconds, "
            else:
                output_string += f"{self.second} second, "

        if self.microsecond > 0:
            if self.microsecond > 1:
                output_string += f"{self.microsecond} microseconds, "
            else:
                output_string += f"{self.microsecond} microsecond, "
        return output_string[:-2]