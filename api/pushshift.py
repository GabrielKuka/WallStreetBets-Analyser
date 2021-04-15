from psaw import PushshiftAPI
from helpers.time import Time

class API:

    def __init__(self):

        self.__api = PushshiftAPI()

    # Return a list
    def last_posts(self, number=1):
        posts = list(self.__api.search_submissions(subreddit='wallstreetbets',
                                             filter=['author', 'title', 'url'],
                                             limit=number))
        return posts

    # Returns a generator 
    def past_days_posts(self, days=1):
        start_time = int(Time.get_past_days(days).timestamp())
        posts = self.__api.search_submissions(subreddit='wallstreetbets',
                                             filter=['author', 'title', 'url'],
                                             after=start_time)
        return posts

