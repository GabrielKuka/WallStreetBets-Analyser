import re

class Validate(object):

    @staticmethod
    def is_ticker_valid(ticker):
        pattern = re.compile("^\$[a-zA-Z]{1,5}$")

        return bool(pattern.match(ticker))