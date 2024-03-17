from datetime import datetime, timedelta, date
from Book import Book

class Promotion():
    def __init__(self, start_date_time, discount):
        day, month, year = map(int, start_date_time.split('/'))
        self.__start_date_time = date(year, month, day) 
        self.__end_date_time = self.__start_date_time + timedelta(days=10)
        self.__discount = discount

    @property
    def start_date_time(self):
        return self.__start_date_time
    
    @property
    def end_date_time(self):
        return self.__end_date_time
    
    @property
    def discount(self):
        return self.__discount

    def check_code_available(self):
        current_day = date.today()
        return self.start_date_time <= current_day <= self.end_date_time

class CoinPromotion(Promotion):
    def __init__(self, start_date_time,discount, code):
        super().__init__(start_date_time,discount)
        self.__code = code

    @property
    def code(self):
        return self.__code


