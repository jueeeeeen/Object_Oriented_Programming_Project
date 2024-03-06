import Book #
import Chapter #
from ChapterTransaction import ChapterTransaction #
from Promotion import CoinPromotion, BookPromotion
import CoinTransaction #
from Reader import Reader, Writer 
from Chapter import Chapter

from dateutil import relativedelta
from datetime import datetime, date, timedelta

class Controller:
    def __init__(self):
        self.__reader_list = []
        self.__writer_list = []
        self.__payment_list = ["OnlineBanking", "Debit Card", "TrueMoney Wallet"]
        self.__promotion_list = []
        self.__report_type_list = ["violence","harrasment"]
        
    @property
    def report_type_list(self):
        return self.__report_type_list
    
    @property
    def reader_list(self):
        return self.__reader_list
    
    @property
    def writer_list(self):
        return self.__writer_list
    
    @property
    def payment_list(self):
        return self.__payment_list
    
    @property
    def all_book_list(self):
        book_list=[]
        for writer in self.__writer_list:
            for book in writer.writing_list:
                book_list.append(book)
        return book_list
    
    def get_all_pseudonym_list(self):
        pseudonym_list = []
        for user in self.__writer_list:
            for pseudonym in user.pseudonym_list:
                pseudonym_list.append(pseudonym)
        return pseudonym_list

    def add_reader(self, reader):
        self.__reader_list.append(reader)
        
    def add_writer(self, writer):
        self.__writer_list.append(writer)
        
    def add_payment(self, payment):
        self.__payment_list.append(payment)

    def add_promotion(self, promotion):
        self.__promotion_list.append(promotion)

    def search_book_by_name(self, book_name):
        search_list=[]
        for book in self.all_book_list:
            if book_name.lower() in book.name.lower():
                search_list.append(book.name)
                
        if search_list==[]:
            return "Not found"
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
        
    def search_coin_promotion(self, code):
        if(code != None):
            for promotion in self.__promotion_list:
                if isinstance(promotion, CoinPromotion) and promotion.code == code:
                    return promotion  
        else: return None
                    
    def get_book_by_name(self, book_name):
        for writer in self.__writer_list:
            for book in writer.writing_list:
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
        for book in self.all_book_list:
            for chapter in book.chapter_list:
                if chapter.chapter_id == chapter_id:
                    return chapter
        return "Chapter Not Found"

    def buy_chapter(self, username, chapter_id):
        user = self.get_user_by_username(username)
        if self.if_user_not_found(user): return user

        chapter = self.get_chapter_by_chapter_id(chapter_id)
        if not isinstance(chapter, Chapter): return chapter
        
        if user.check_repeated_purchase(chapter): return "You have already purchased this chapter."
        
        cost = chapter.cost

        coin_balance = user.get_user_coin_balance()

        if coin_balance >= cost:
            user.deduct_coin(cost)
            user.add_chapter_transaction_list(ChapterTransaction(chapter, cost))
            return "Your purchase was successful"
        else:
            return "Not enough coin"
        
    def show_coin(self, username):
        user = self.get_user_by_username(username)
        if self.if_user_not_found(user): return user
        if user:
            return {"Golden Coin" : user.golden_coin.balance, "Silver Coin" : user.get_silver_coin_balance()}
        return "User Not Found"
    
    # def sign_in(self,username, password):
    #     user = self.get_user_by_username(username)
    #     print(user.username, user.password, user.birth_date)
    #     if (isinstance(user,Reader) or isinstance(user,Writer)):
    #         if user.password == password:
    #             return "log in successfully"
    #         else: 
    #             return "wrong password"
    #     else:
    #         return "can not find username/password"
    
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
        writing_list = "-"
        pseudonym_list = "-"
        comment_list = "-"
        user = self.get_user_by_username(username)
        if isinstance(user, Writer):
            writing_count = len(user.writing_list)
            reads = user.get_viewer_count()
            writing_list = user.show_writing_name_list()
            pseudonym_list = user.pseudonym_list
            comment_list = user.get_json_comment_list()
        else:
            if self.if_user_not_found(user): return user
        return {"display_name" : user.display_name,
                "username" : user.username,
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
        if self.if_user_not_found(user): return user
        return {"display_name" : user.display_name,
                "username" : user.username,
                "password" : "******",
                "menu" : ["change password",
                            "go to page",
                            "upgrade to writer",
                            "pseudonym",
                            "verify age"]}
        
    def show_my_reading(self, username):
        user = self.get_user_by_username(username)
        if self.if_user_not_found(user): return user
        reading_list = []
        for book in user.get_book_shelf_list():
            reading = {"name" : book.name,
                       "tags" : book.tag,
                       "status" : book.status,
                       "prologue" : book.prologue}
            reading_list.append(reading)
        return reading_list

    def change_password(self, username, old_password, new_password):
        user = self.get_user_by_username(username)
        if self.if_user_not_found(user): return user
        if user.password == old_password and len(new_password) >= 8:
            user.password = new_password
            return "Password has been changed"
        elif user.password != old_password:
            return "Wrong password"
        elif len(new_password) < 8:
            return "Password must be at least 8 letters"
        else:
            return "Please try again"
        
    def change_display_name(self, username, new_display_name):
        user = self.get_user_by_username(username)
        user.display_name = new_display_name
        return "display name has been changed"
    
    def add_pseudonym(self, username, pseudonym):
        user = self.get_user_by_username(username)
        if self.if_user_not_found(user): return user
        if self.check_repeated_pseudonym(pseudonym):
            return "pseudonym already exists"
        user.add_pseudonym(pseudonym)
        return "pseudonym added"
    
    def check_repeated_pseudonym(self, new_pseudonym):
        for pseudonym in self.get_all_pseudonym_list():
            if pseudonym.lower() == new_pseudonym.lower():
                return True
        return False
    
    def if_user_not_found(self, user):
        if not (isinstance(user, Reader) or isinstance(user, Writer)):
            return True
        return False
    
    # def buy_coin(self, username, payment, code, golden_amount):
    #     price = golden_amount
    #     silver_amount = int(golden_amount * 10 / 100)
    #     user = self.get_user_by_username(username)
    #     coin_promotion = self.search_coin_promotion(code)
        
    #     if(code != None and coin_promotion != None):
    #         print("Applying code")
    #         price = (100 - coin_promotion.discount) / 100 * price #ลดราคา 
    #     elif(coin_promotion != None):
    #             return "Your code is expired or not exist"
    #     else:
    #         print("Not applying any code")
            
    #     self.add_coin_to_user(user, payment, golden_amount, silver_amount, price)
    
    # def create_book(self, name:str, writer_name:str, tag_list: str, status: str, age_restricted: bool, prologue: str):
    #     writer = self.get_user_by_username(writer_name)
    #     book = self.get_book_by_name(name)
    #     if isinstance(writer,Writer) and isinstance(book,Book) == False:
    #         new_book = Book(name,writer,tag_list,status,age_restricted,prologue)
    #         writer.add_writing_book_list(new_book)
    #         return {"Book": "create book successfully"}
    #     else : 
    #         return {"Book": "please try again"}
    
    # def create_chapter(self,book_name,chapter_number, name, context, cost):
    #     book = self.get_book_by_name(book_name)
    #     if isinstance(book,Book) and book.is_chapter_valid(chapter_number):
    #         chapter = Chapter(book_name,chapter_number, name, context, cost)
    #         book.add_chapter_list(chapter)
    #         return {"Chapter": "create Chapter successfully"}
    #     else : 
    #         return {"Chapter": "please try again"}   
        
    # def create_comment(self, chapter_id, username, context):
    #     chapter = self.search_chapter_by_chapter_id(chapter_id)
    #     user = self.get_user_by_username(username)
    #     # print(chapter)
    #     if isinstance(chapter,Chapter):
    #         new_comment = Comment(chapter,user,context)
    #         #find book and append in book 
    #         chapter.add_comment(new_comment)
    #         return {"Comment": "create comment success"}
    #     else : 
    #         return {"Comment": "please try again"}
        
    # # รับ username มาด้วยดีมั้ย แล้วเพิ่มpaymentmethodไว้ในuserแต่ละคน  
    # def create_payment_method(self, payment_method_name, payment_info):
    #     if payment_method_name == self.__payment_list[0]:
    #         return OnlineBanking(payment_info)
    #     elif payment_method_name == self.__payment_list[1]:
    #         return DebitCard(payment_info)
    #     elif payment_method_name == self.__payment_list[2]:
    #         return TrueMoneyWallet(payment_info)
            
    # def edit_book_info(self, name, add_tag_list, delete_tag_list, status, age_restricted, prologue):
    #     book = self.get_book_by_name(name)
    #     if name:
    #         book.name=name
    #     if add_tag_list:
    #         book.add_tag(add_tag_list)
    #     if delete_tag_list:
    #         book.delete_tag(delete_tag_list)
    #     if status:
    #         book.status = status
    #     if age_restricted:
    #         book.age_restricted = age_restricted
    #     if prologue:
    #         book.prologue = prologue
    #     # book.date_time(0)
    #     return book
            
    # def edit_chapter_info(self,chapter_id, name, context, cost):
    #     chapter = self.search_chapter_by_chapter_id(chapter_id)
    #     if name:
    #         chapter.name=name
    #     if context:
    #         chapter.context(context)
    #     if cost:
    #         chapter.cost(cost)
    #     # chapter.publish_date_time(0)
    #     return chapter
    
    