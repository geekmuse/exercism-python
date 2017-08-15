from datetime import date
import calendar

"""Set Sunday to first day of week for calendar module (defaults to Monday)"""
calendar.setfirstweekday(calendar.SUNDAY)

"""Define custom exception class"""
class MeetupDayException(Exception):
    pass


def meetup_day(year, month, day, ord_date):
    """
    Compute date based on "meetup day"-type date listings

    :param year: Year of meetup (YYYY)
    :param month: Month of meetup (MM)
    :param day: Day (of week) of meetup (e.g. 'Sunday', 'Monday', etc.)
    :param ord_date: Ordinal prefix for day (e.g. '3rd', '4th') - combine with "day" to get "3rd Sunday"...
    :return: datetime.date object representing best guess at date
    """
    calendar_matrix = calendar.monthcalendar(year, month)
    idx_weekday = index_from_weekday(day)
    # If ord_date is 'last', start with the last week of the month
    # and work backwards.
    if ord_date == 'last':
        cal_row = len(calendar_matrix)-1
        if calendar_matrix[cal_row][idx_weekday] == 0:
            cal_row -= 1
        date_guess = calendar_matrix[cal_row][index_from_weekday(day)]

    # If ord_date is 'teenth', this is the trickiest case.  Start with second week
    # of the month and iterate up by one week at a time, until we find the right
    # date using our 'teenth' interval (13 >= x >= 19) as a guide.
    elif ord_date == 'teenth':
        cal_row = 1
        date_guess = calendar_matrix[cal_row][index_from_weekday(day)]
        while date_guess < 13 and not date_guess > 19:
            cal_row += 1
            date_guess = calendar_matrix[cal_row][index_from_weekday(day)]

    # For the generic case, start with the week of the month that matches the ord_date.
    # E.g. if "first Sunday" start with week 1; if date is a 0 (what calendar module returns
    # if the date isn't in the month), then bump up one week.  If new row doesn't exist in calendar,
    # throw an exception.
    else:
        cal_row = int(ord_date[:-2])-1
        try:
            if calendar_matrix[cal_row][idx_weekday] == 0 or calendar_matrix[0][idx_weekday] == 0:
                cal_row += 1
            date_guess = calendar_matrix[cal_row][index_from_weekday(day)]
        except Exception:
            raise MeetupDayException()

    # Make a guess; if it doesn't match up, throw an exception.
    datetime_guess = date(year, month, date_guess)
    if calendar.day_name[datetime_guess.weekday()] == day:
        return datetime_guess
    else:
        raise MeetupDayException()


def index_from_weekday(weekday):
    """
    Returns a numeric index for day of week based on name of day

    :param weekday: Name of day (e.g. 'Sunday', 'Monday', etc.)
    :return: numeric index
    """
    weekday_map = {
        'Sunday': 0,
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday': 4,
        'Friday': 5,
        'Saturday': 6
    }

    return weekday_map.get(weekday)
