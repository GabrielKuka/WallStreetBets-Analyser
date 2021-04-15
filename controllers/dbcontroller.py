from db.handledb import DB
from helpers.validate import Validate
from api.pushshift import API

class DbController:

    def __init__(self):
        self.__db = DB() 

        self.__api = API()

        self.__check_table()

    def last_posts(self, number=5):
        return self.__api.last_posts(number)

    def past_days_posts(self, number=1):
        return self.__api.past_days_posts(number)

    def most_common_stocks(self, number=5):
        if self.__db.is_table_empty():
            posts = self.past_days_posts()
            self.populate_table(posts)

        # Get the results
        rows = self.__db.get_most_common_stocks(number)
        print("The most popular stocks in WallStreetBets:")
        for row in rows:
            print(row[0])
        print('\n')

    def most_popular_stock(self):
        if self.__db.is_table_empty():
            posts = self.past_days_posts()
            self.populate_table(posts)

        # Get the result
        stonk = self.__db.get_most_common_stocks()
        print("The most popular stock in WallStreetBets is {}".format(stonk))
        print('\n')
            
    def __check_table(self):
        if not self.__db.is_table_empty():
            self.__db.wipe_table()

    def populate_table(self, posts):
        print("Retrieving data. Please wait..")
        for post in posts:
            words = post.title.split()
            tickers = list(set(filter(lambda word: Validate.is_ticker_valid(word), words)))

            if len(tickers) > 0:
                for ticker in tickers:
                    #submitted_time = datetime.datetime.fromtimestamp(post.created_utc).isoformat()
                    self.__db.update_table(ticker)