from datetime import timedelta

def add_gigasecond(datetime_obj):
    return datetime_obj + timedelta(seconds=1e9)
