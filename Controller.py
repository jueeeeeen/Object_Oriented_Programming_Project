import Book
import Chapter
import ChapterTransaction
import CoinTransaction
from Reader import Reader, Writer
from Book import Book
from Chapter import Chapter


class Controller:
    def __init__(self):
        self.__reader_list = []
        self.__writer_list = []
        self.__payment_list = []
        self.__promotion_list = []
        self.__report_type_list = ["violence","harrasment"]

    def add_reader(self, reader):
        self.__reader_list.append(reader)

    def get_all_book_list(self):
        book_list=[]
        for writer in self.__writer_list:
            for book in writer.writing_list:
                book_list.append(book)
        return book_list

    def search_book_by_name(self, book_name):
        search_list=[]
        for writer in self.__writer_list:
            for book in writer.writing_book_list:
                if book_name.lower() in book.name.lower():
                    search_list.append(book.name)
                    
        if search_list==[]:
            return "huhuuuu"
        else:
            return search_list
          
    def search_user(self, username):
        search_list = []
        for reader in self.__reader_list:
            if username.lower() in reader.username.lower():
                search_list.append(reader.username)
        
        for writer in self.__writer_list:
            if username.lower() in writer.username.lower() and writer.username not in search_list:
                search_list.append(writer.username)

        if search_list == []:
            return "user not found"
        else:
            return search_list
                    
    def get_book_by_name(self, book_name):
        for writer in self.__writer_list:
            for book in writer.book:
                if book.name == book_name:
                    return book
        return "Book Not Found"
                
    def get_user_by_username(self, username):
        for reader in self.__reader_list:
            if reader.username == username:
                return reader
        
        for writer in self.__writer_list:
            if writer.username == username:
                return writer
            
        return "User Not Found"
    
    def get_chapter_by_chapter_id(self, chapter_id):
        for book in self.get_all_book_list():
            for chapter in book.chapter_list:
                if chapter.chapter_id == chapter_id:
                    return chapter
        return "Chapter Not Found"

    @property
    def report_type_list(self):
        return self.__report_type_list

    def search_coin_promotion(self, code):
        pass

    def add_writer(self, writer):
        self.__writer_list.append(writer)

    def add_payment(self, payment):
        self.__payment_list.append(payment)

    def add_promotion(self, promotion):
        self.__promotion_list.append(promotion)

    def buy_chapter(self, username, chapter_id):
        user = self.get_user_by_username(username)
        if self.is_user_not_found(user): return user

        chapter = self.get_chapter_by_chapter_id(chapter_id)
        if not isinstance(chapter, Chapter): return chapter
        cost = chapter.cost

        coin_balance = user.get_user_coin_balance()

        if coin_balance >= cost:
            user.deduct_coin(cost)
            # user.add_chapter_transaction()
            return "Done"
        else:
            return "Not enough coin"
        
    def show_coin(self, username):
        user = self.get_user_by_username(username)
        if self.is_user_not_found(user): return user
        if user:
            return {"Golden Coin" : user.golden_coin.balance, "Silver Coin" : user.get_silver_coin_balance()}
        return "User Not Found"
    
    def sign_up(self,username:str, password:str, birth_date: str):
        new_reader = Reader(username,password,birth_date)
        if isinstance(new_reader, Reader):
            self.add_reader(new_reader)
            return {"User": "sign up success"}
        else : 
            return {"User": "please try again"}
        
    def show_my_page(self, username):
        writing_count = 0
        reads = 0
        writing_list = None
        pseudonym_list = None
        comments = None
        user = self.get_user_by_username(username)
        if isinstance(user, Writer):
            writing_count = len(user.get_writing_list())
            reads = user.get_viewer_count()
            writing_list = user.show_writing_name_list()
            pseudonym_list = user.pseudonym_list
            comment_list = user.get_json_comment_list()
        else:
            if self.is_user_not_found(user): return user
        return {"display_name" : user.display_name,
                "introduction" : user.introduction,
                "writing_count" : writing_count,
                "book_on_shelf_count" : len(user.get_book_shelf_list()),
                "followers" : len(user.get_follower_list()),
                "read_count" : len(user.recent_read_chapter_list),
                "viewer_count" : reads,
                "writings" : writing_list,
                "pseudonyms" : pseudonym_list,
                "comments" : comment_list}
    
    def show_my_profile(self, username):
        user = self.get_user_by_username(username)
        if self.is_user_not_found(user): 
            return user
        return {"username" : user.username,
                "password" : "******",
                "menu" : ["change password",
                            "go to page",
                            "upgrade to writer",
                            "pseudonym",
                            "verify age"]}

    def change_password(self, username, new_password):
        user = self.get_user_by_username(username)
        if self.is_user_not_found(user): return user
        user.password = new_password
        return "Password has been changed"
    
    def get_all_pseudonym_list(self, username):
        pseudonym_list = []
        for user in self.__writer_list:
            for pseudonym in user.pseudonym_list:
                pseudonym_list.append(pseudonym)
        return pseudonym_list
    
    def repeated_pseudonym(self, new_pseudonym):
        for pseudonym in self.get_all_pseudonym_list():
            if pseudonym.lower() == new_pseudonym.lower():
                return True
        return False
    
    def add_pseudonym(self, username, pseudonym):
        user = self.get_user_by_username(username)
        if self.is_user_not_found(user): return user
        if self.repeated_pseudonym(pseudonym):
            return "pseudonym already exists"
        user.add_pseudonym(pseudonym)
        return "pseudonym added"

    def show_my_reading(self, username):
        user = self.get_user_by_username(username)
        if self.is_user_not_found(user): return user
        reading_list = []
        for book in user.recent_read_chapter_list:
            reading_list.append(book)
        return reading_list
    
    def is_user_not_found(self, user):
        if not (isinstance(user, Reader) or isinstance(user, Writer)):
            return True
        return False
    
    