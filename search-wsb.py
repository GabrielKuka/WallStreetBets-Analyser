from psaw import PushshiftAPI
from controllers.dbcontroller import DbController

class WSBTracker:

    def __init__(self):
        self.controller = DbController()
    
    def menu(self):
        print("\n\n\t\t~~~ Welcome to WallStreetBets tracker! ~~~\n")
        while True:
            print('1. Get last 5 posts.')
            print('2. Get last 10 posts.')
            print('3. Get the 5 most popular stocks in WSB from past day.')
            print('4. Get the most popular stock in WSB form past day.')
            print('5. Exit')

            cmd = int(input("> "))
            if cmd == 5:                    
                quit()
            elif cmd == 4:
                self.controller.most_popular_stock()
            elif cmd == 3:
                self.controller.most_common_stocks()
            elif cmd == 2:                    
                posts = self.controller.last_posts(10)
                self.print_posts(posts)
            elif cmd == 1:                    
                posts = self.controller.last_posts(5)
                self.print_posts(posts)
        
    def print_posts(self, posts):
        for post in posts:
                print("Author: {}".format(post.author))
                print("Title: {}".format(post.title))
                print("Url: {}".format(post.url))
                print("~~~")


tracker = WSBTracker()
tracker.menu()