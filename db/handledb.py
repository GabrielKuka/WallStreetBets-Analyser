import psycopg2, psycopg2.extras, config

class DB:

    def __init__(self):
        self.__connection = psycopg2.connect(host=config.DB_HOST,
                                            database=config.DB_NAME,
                                            user=config.DB_USER,
                                            password=config.DB_PASS)

        self.__cursor = self.__connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    def get_cursor(self):
        # Check if there is a connection
        if type(self.__connection) is None:
            raise Exception('Connection to db not established.')
        elif type(self.__cursor) is None:
            raise Exception('Cursor not initialized.')

        return self.__cursor

    def is_table_empty(self):
        query = "select count(1) from mention"
        try:
            self.get_cursor().execute(query)
        except Exception as e:
            print(e)
        else:
            if self.get_cursor().fetchone()[0] > 0:
                return False
            return True

    def wipe_table(self):
        query = "DELETE FROM mention;" 
        try:
            self.get_cursor().execute(query)
            self.__connection.commit()
        except Exception as e:
            print(e)
            self.__connection.rollback()
    
    def update_table(self, ticker):
        query = "INSERT INTO mention (ticker, mentions) VALUES('{}', 1)\
        ON CONFLICT (ticker) DO UPDATE SET mentions=mention.mentions+1".format(ticker.upper())
        try:
            self.get_cursor().execute(query)
            self.__connection.commit()
        except Exception as e:
            print(e)
            self.__connection.rollback()

    def get_most_common_stocks(self, number=1):
        query = "SELECT ticker FROM mention ORDER BY mentions DESC LIMIT {}".format(number)
        self.get_cursor().execute(query)

        if number == 1:
            return self.get_cursor().fetchone()[0]

        return self.get_cursor().fetchall()