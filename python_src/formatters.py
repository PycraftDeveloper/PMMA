import math as _math

from pmma.python_src.constants import Constants

from pmma.python_src.utility.general_utils import initialize as _initialize

class TimeFormatter:
    def __init__(self):
        _initialize(self)

        self._years = 0
        self._months = 0
        self._days = 0
        self._hours = 0
        self._minutes = 0
        self._seconds = 0
        self._microseconds = 0

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

        self._years = years
        self._months = months
        self._days = days
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        self._microseconds = microseconds

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

        self._years = years
        self._months = months
        self._days = days
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        self._microseconds = microseconds

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

        self._years = years
        self._months = months
        self._days = days
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        self._microseconds = microseconds

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

        self._years = years
        self._months = months
        self._days = days
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        self._microseconds = microseconds

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

        self._years = years
        self._months = months
        self._days = days
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        self._microseconds = microseconds

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

        self._years = years
        self._months = months
        self._days = days
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        self._microseconds = microseconds

    def set_from_microsecond(self, microsecond):
        # Convert microseconds to seconds
        seconds_float = microsecond / Constants.MICROSECONDS_PER_SECOND

        # Use the seconds conversion function
        return self.set_from_second(seconds_float)

    def get_year(self):
        return self._years

    def get_month(self):
        return self._months

    def get_day(self):
        return self._days

    def get_hour(self):
        return self._hours

    def get_minute(self):
        return self._minutes

    def get_second(self):
        return self._seconds

    def get_microsecond(self):
        return self._microseconds

    def get_in_date_format(self):
        return f"{self._days}/{self._months}/{self._years} @ {self._hours}:{self._minutes}:{self._seconds}.{self._microseconds}"

    def get_in_sentence_format(self):
        output_string = ""
        if self._years > 0:
            if self._years > 1:
                output_string += f"{self._years} years, "
            else:
                output_string += f"{self._years} year, "

        if self._months > 0:
            if self._months > 1:
                output_string += f"{self._months} months, "
            else:
                output_string += f"{self._months} month, "

        if self._days > 0:
            if self._days > 1:
                output_string += f"{self._days} days, "
            else:
                output_string += f"{self._days} day, "

        if self._hours > 0:
            if self._hours > 1:
                output_string += f"{self._hours} hours, "
            else:
                output_string += f"{self._hours} hour, "

        if self._minutes > 0:
            if self._minutes > 1:
                output_string += f"{self._minutes} minutes, "
            else:
                output_string += f"{self._minutes} minute, "

        if self._seconds > 0:
            if self._seconds > 1:
                output_string += f"{self._seconds} seconds, "
            else:
                output_string += f"{self._seconds} second, "

        if self._microseconds > 0:
            if self._microseconds > 1:
                output_string += f"{self._microseconds} microseconds.  "
            else:
                output_string += f"{self._microseconds} microsecond.  "

        output_string = " and ".join(output_string[:-2].rsplit(", ", 1))
        return output_string