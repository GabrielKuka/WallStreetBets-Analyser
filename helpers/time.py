from datetime import datetime, timedelta

class Time(object):

    @staticmethod
    def get_past_hours(hours=1):
        return datetime.now() - timedelta(hours=hours)

    @staticmethod
    def get_past_days(days=1):
        return datetime.now() - timedelta(days=days)