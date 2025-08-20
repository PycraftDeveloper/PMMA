import math

from pmma.core.py_src.Constants import InternalConstants

class TimeFormatter:
    def __init__(self):
        self._years = 0
        self._months = 0
        self._days = 0
        self._hours = 0
        self._minutes = 0
        self._seconds = 0
        self._microseconds = 0

    def set_from_year(self, year):
        # Convert to total seconds
        total_seconds = year * InternalConstants.DAYS_PER_YEAR * InternalConstants.SECONDS_PER_DAY

        # Years
        years = math.floor(year)
        remainder_seconds = total_seconds - (years * InternalConstants.DAYS_PER_YEAR * InternalConstants.SECONDS_PER_DAY)

        # Months
        month = remainder_seconds / (InternalConstants.DAYS_PER_MONTH * InternalConstants.SECONDS_PER_DAY)
        months = math.floor(month)
        remainder_seconds -= months * InternalConstants.DAYS_PER_MONTH * InternalConstants.SECONDS_PER_DAY

        # Days
        day = remainder_seconds / InternalConstants.SECONDS_PER_DAY
        days = math.floor(day)
        remainder_seconds -= days * InternalConstants.SECONDS_PER_DAY

        # Hours
        hour = remainder_seconds / InternalConstants.SECONDS_PER_HOUR
        hours = math.floor(hour)
        remainder_seconds -= hours * InternalConstants.SECONDS_PER_HOUR

        # Minutes
        minute = remainder_seconds / InternalConstants.SECONDS_PER_MINUTE
        minutes = math.floor(minute)
        remainder_seconds -= minutes * InternalConstants.SECONDS_PER_MINUTE

        # Seconds
        seconds = math.floor(remainder_seconds)
        remainder_seconds -= seconds

        # Microseconds
        microseconds = math.floor(remainder_seconds * 1e6)

        self._years = years
        self._months = months
        self._days = days
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        self._microseconds = microseconds

    def set_from_month(self, month):
        # Years
        years = math.floor(month / 12)
        months_remainder = month - years * 12

        # Months
        months = math.floor(months_remainder)
        day = (months_remainder - months) * InternalConstants.DAYS_PER_MONTH
        days = math.floor(day)

        # Remainder in seconds
        remainder_seconds = (day - days) * InternalConstants.SECONDS_PER_DAY

        # Hours
        hours = math.floor(remainder_seconds / InternalConstants.SECONDS_PER_HOUR)
        remainder_seconds -= hours * InternalConstants.SECONDS_PER_HOUR

        # Minutes
        minutes = math.floor(remainder_seconds / InternalConstants.SECONDS_PER_MINUTE)
        remainder_seconds -= minutes * InternalConstants.SECONDS_PER_MINUTE

        # Seconds
        seconds = math.floor(remainder_seconds)
        remainder_seconds -= seconds

        # Microseconds
        microseconds = math.floor(remainder_seconds * 1e6)

        self._years = years
        self._months = months
        self._days = days
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        self._microseconds = microseconds

    def set_from_day(self, day):
        # Years
        years = math.floor(day / InternalConstants.DAYS_PER_YEAR)
        days_remainder = day - years * InternalConstants.DAYS_PER_YEAR

        # Months
        months = math.floor(days_remainder / InternalConstants.DAYS_PER_MONTH)
        days_remainder -= months * InternalConstants.DAYS_PER_MONTH

        # Days
        days = math.floor(days_remainder)

        # Remainder in seconds
        remainder_seconds = (days_remainder - days) * InternalConstants.SECONDS_PER_DAY

        # Hours
        hours = math.floor(remainder_seconds / InternalConstants.SECONDS_PER_HOUR)
        remainder_seconds -= hours * InternalConstants.SECONDS_PER_HOUR

        # Minutes
        minutes = math.floor(remainder_seconds / InternalConstants.SECONDS_PER_MINUTE)
        remainder_seconds -= minutes * InternalConstants.SECONDS_PER_MINUTE

        # Seconds
        seconds = math.floor(remainder_seconds)
        remainder_seconds -= seconds

        # Microseconds
        microseconds = math.floor(remainder_seconds * 1e6)

        self._years = years
        self._months = months
        self._days = days
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        self._microseconds = microseconds

    def set_from_hour(self, hour):
        # Years
        days_float = hour / InternalConstants.HOURS_PER_DAY
        years = math.floor(days_float / InternalConstants.DAYS_PER_YEAR)
        days_remainder = days_float - years * InternalConstants.DAYS_PER_YEAR

        # Months
        months = math.floor(days_remainder / InternalConstants.DAYS_PER_MONTH)
        days_remainder -= months * InternalConstants.DAYS_PER_MONTH

        # Days
        days = math.floor(days_remainder)
        hours_remainder = (days_remainder - days) * InternalConstants.HOURS_PER_DAY

        # Hours
        hours = math.floor(hours_remainder)
        minute = (hours_remainder - hours) * InternalConstants.SECONDS_PER_HOUR / InternalConstants.SECONDS_PER_MINUTE

        # Minutes
        minutes = math.floor(minute)
        remainder_seconds = (minute - minutes) * InternalConstants.SECONDS_PER_MINUTE

        # Seconds
        seconds = math.floor(remainder_seconds)
        remainder_seconds -= seconds

        # Microseconds
        microseconds = math.floor(remainder_seconds * 1e6)

        self._years = years
        self._months = months
        self._days = days
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        self._microseconds = microseconds

    def set_from_minute(self, minute):
        # Years
        hours_float = minute / InternalConstants.MINUTES_PER_HOUR
        days_float = hours_float / InternalConstants.HOURS_PER_DAY
        years = math.floor(days_float / InternalConstants.DAYS_PER_YEAR)
        days_remainder = days_float - years * InternalConstants.DAYS_PER_YEAR

        # Months
        months = math.floor(days_remainder / InternalConstants.DAYS_PER_MONTH)
        days_remainder -= months * InternalConstants.DAYS_PER_MONTH

        # Days
        days = math.floor(days_remainder)
        hours_float = (days_remainder - days) * InternalConstants.HOURS_PER_DAY

        # Hours
        hours = math.floor(hours_float)
        minutes_remainder = (hours_float - hours) * InternalConstants.MINUTES_PER_HOUR

        # Minutes
        minutes = math.floor(minutes_remainder)
        remainder_seconds = (minutes_remainder - minutes) * InternalConstants.SECONDS_PER_MINUTE

        # Seconds
        seconds = math.floor(remainder_seconds)
        remainder_seconds -= seconds

        # Microseconds
        microseconds = math.floor(remainder_seconds * 1e6)

        self._years = years
        self._months = months
        self._days = days
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        self._microseconds = microseconds

    def set_from_second(self, second):
        # Years
        days_float = second / InternalConstants.SECONDS_PER_DAY
        years = math.floor(days_float / InternalConstants.DAYS_PER_YEAR)
        days_remainder = days_float - years * InternalConstants.DAYS_PER_YEAR

        # Months
        months = math.floor(days_remainder / InternalConstants.DAYS_PER_MONTH)
        days_remainder -= months * InternalConstants.DAYS_PER_MONTH

        # Days
        days = math.floor(days_remainder)
        hours_float = (days_remainder - days) * InternalConstants.HOURS_PER_DAY

        # Hours
        hours = math.floor(hours_float)
        minutes_float = (hours_float - hours) * InternalConstants.MINUTES_PER_HOUR

        # Minutes
        minutes = math.floor(minutes_float)
        remainder_seconds = (minutes_float - minutes) * InternalConstants.SECONDS_PER_MINUTE

        # Seconds
        seconds = math.floor(remainder_seconds)
        remainder_seconds -= seconds

        # Microseconds
        microseconds = math.floor(remainder_seconds * 1e6)

        self._years = years
        self._months = months
        self._days = days
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        self._microseconds = microseconds

    def set_from_microsecond(self, microsecond):
        # Convert microseconds to seconds
        seconds_float = microsecond / InternalConstants.MICROSECONDS_PER_SECOND

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