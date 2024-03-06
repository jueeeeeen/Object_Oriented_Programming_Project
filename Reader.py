#Reader.py
from datetime import datetime, date, timedelta
from dateutil import relativedelta
import Book
import Chapter
from Coin import SilverCoin, GoldenCoin
import ChapterTransaction
from CoinTransaction import CoinTransaction

class Reader:
    def __init__(self,username,password,birth_date):
        self.__username = username
        self.__display_name = username
        self.__password = password
        self.__birth_date = birth_date #check age_restricted
        self.__golden_coin = GoldenCoin(0)
        self.__silver_coin_list = []
        self.__book_shelf_list = []
        self.__recent_read_chapter_list = []
        self.__chapter_transaction_list = []
        self.__coin_transaction_list = []
        self.__follower_list = []
        self.__introduction = ''
    
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,username):
        self.__username = username

    @property
    def display_name(self):
        return self.__display_name
    @display_name.setter
    def display_name(self, display_name):
        self.__display_name = display_name

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,password):
        self.__password = password

    @property
    def birth_date(self):
        return self.__birth_date
    
    @property
    def follower_list(self):
        return self.__follower_list
    
    def get_user_coin_balance(self):
        return self.__golden_coin.balance + self.get_silver_coin_balance()
    
    def get_silver_coin_balance(self):
        silver_coin_balance = 0
        for silver_coin in self.__silver_coin_list:
            silver_coin_balance += silver_coin.balance
        return silver_coin_balance
    
    def show_silver_coin_list(self):
        silver_coin_dict = {}
        for silver_coin in self.__silver_coin_list:
            if not silver_coin_dict.get(silver_coin.exp_date_time):
                silver_coin_dict[silver_coin.exp_date_time] = []
            silver_coin_dict[silver_coin.exp_date_time].append(silver_coin.balance)
        return silver_coin_dict
    
    @property
    def golden_coin(self):
        return self.__golden_coin
    
    @property
    def introduction(self):
        return self.__introduction
    @introduction.setter
    def introduction(self, text):
        self.__introduction = text
    
    def add_golden_coin(self,amount):
        self.golden_coin.balance += amount
    def deduct_golden_coin(self,amount):
        self.golden_coin.balance -= amount
    
    def get_silver_coin_list(self):
        return self.__silver_coin_list

    def add_silver_coin(self,amount):
        self.__silver_coin_list.append(SilverCoin(amount))

    def delete_silver_coin(self):
        for silver_coin in self.__silver_coin_list:
            if (silver_coin.exp_date_time - datetime.today() == -1) or (silver_coin.balance == 0):
                self.__silver_coin_list.remove(silver_coin)

    def deduct_coin(self, amount):
        for silver_coin in self.__silver_coin_list:
            if amount != 0 or self.__silver_coin_list != []:
                transac_amount = silver_coin.deduct_silver_coin(amount)
                amount -= transac_amount
                print(f"amount : {amount}\ntransac_amount : {transac_amount}")
                self.delete_silver_coin()
                # self.add_coin_transaction(CoinTransaction.CoinTransaction(None, None, transac_amount, self.get_user_coin_balance(), datetime.now()))
            else:
                break
        if amount != 0:
            self.golden_coin.deduct_golden_coin(amount)
            # self.add_coin_transaction(CoinTransaction.CoinTransaction(None, None, amount, self.get_user_coin_balance(), datetime.now()))
        return "Done"

    def get_book_shelf_list(self):
        return self.__book_shelf_list
    def add_book_shelf_list(self,book):
        if isinstance(book,Book.Book):
            self.__book_shelf_list.append(book)
        
    def get_follower_list(self):
        return self.__follower_list

    @property
    def recent_read_chapter_list(self):
        return self.__recent_read_chapter_list
    def add_recent_read_chapter_list(self,chapter):
        if isinstance(chapter,Chapter.Chapter):
            self.__recent_read_chapter_list.append(chapter)

    def get_chapter_transaction_list(self):
        return self.__chapter_transaction_list
    def add_chapter_transaction_list(self,chapter_transaction):
        if isinstance(chapter_transaction,ChapterTransaction):
            self.__chapter_transaction_list.append(chapter_transaction)
    
    def get_coin_transaction_list(self):
        return self.__coin_transaction_list
    def add_coin_transaction_list(self,coin_transaction):
        if isinstance(coin_transaction,CoinTransaction):
            self.__coin_transaction_list.append(coin_transaction)

    def check_age_restricted(self):
        day, month, year = map(int, self.__birth_date.split('/'))
        birth = datetime(year, month, day)
        date_diff = relativedelta.relativedelta(datetime.now(),birth)
        if date_diff.years>=18 :
            return "over 18"
        else: 
            return "under 18"
        
    def show_coin_transaction(self):
        show_list = []
        for coin_transaction in self.__coin_transaction_list:
            payment_type = coin_transaction.payment.name
            golden_amount = coin_transaction.golden_amount
            silver_amount = coin_transaction.silver_amount
            price = coin_transaction.price
            date_time = coin_transaction.date_time
            show_list.append(f"{payment_type} +{golden_amount}_golden_coin +{silver_amount}_silver_coin -{price} baht at {date_time}")
        return show_list


class Writer(Reader):
    money_balance = 0
    def __init__(self,username,password,birth_date):
        super().__init__(username,password,birth_date)
        self.__writing_book_list = []
        self.__pseudonym_list = []
    
    @property
    def writing_list(self):
        return self.__writing_book_list
    
    def show_writing_name_list(self):
        writing_name_list = []
        for book in self.__writing_book_list:
            writing_name_list.append(book.name)
        return writing_name_list
    
    def add_writing_book_list(self,book):
        if isinstance(book,Book.Book):
            self.__writing_book_list.append(book)

    @property
    def pseudonym_list(self):
        return self.__pseudonym_list
    
    def add_pseudonym(self, pseudonym):
        self.__pseudonym_list.append(pseudonym)

    def repeated_pseunonym(self, new_pseudonym):
        for pseudonym in self.__pseudonym_list:
            if pseudonym.lower() == new_pseudonym.lower():
                return True
        return False

    def get_viewer_count(self):
        count = 0
        for book in self.__writing_book_list:
            for chapter in book.chapter_list():
                count += chapter.viewer_count
        return count
    
    def get_comment_list(self):
        comment_list = []
        for book in self.__writing_book_list:
            comment_list.append(book.comment_list())
        return comment_list
    
    def get_json_comment_list(self):
        comment_list = []
        for book in self.__writing_book_list:
            for comment in book.comment_list():
                comment_dict = {}
                comment_dict["user"] = comment.commentator.name
                comment_dict["context"] = comment.context
                comment_dict["chapter"] = f"#{comment.chapter.chapter_number} : {comment.chapter.name}"
                comment_dict["date_time"] = comment.publish_date_time
                comment_list.append(comment_dict)
        return comment_list