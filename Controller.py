from Book import Book #
from Chapter import Chapter #
from Comment import Comment #
from Reader import Reader, Writer 
from CoinTransaction import CoinTransaction #
from ChapterTransaction import ChapterTransaction #
from Promotion import CoinPromotion, BookPromotion
from Payment import OnlineBanking, TrueMoneyWallet, DebitCard
from datetime import datetime
from Report import Report

class Controller:
    def __init__(self):
        self.__reader_list = []
        self.__writer_list = []
        self.__payment_list = ["OnlineBanking", "Debit Card", "TrueMoney Wallet"]
        self.__promotion_list = []
        self.__report_type_list = ["violence", "harrasment"]
    
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Sub Methods <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # ____________________________________Getters___________________________________
    
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
    def report_type_list(self):
        return self.__report_type_list
    
    @property
    def all_book_list(self):
        book_list=[]
        for writer in self.__writer_list:
            for book in writer.writing_list:
                book_list.append(book)
        return book_list
    
    @property
    def all_pseudonym_list(self):
        pseudonym_list = []
        for user in self.__writer_list:
            for pseudonym in user.pseudonym_list:
                pseudonym_list.append(pseudonym)
        return pseudonym_list
    
    def get_book_by_name(self, book_name):
        for book in self.all_book_list:
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
    
    def get_chapter_by_chapter_id_or_book(self, chapter_id):
        if "-" in chapter_id:
            return self.get_chapter_by_chapter_id(chapter_id)
        elif isinstance(self.get_book_by_name(chapter_id),Book):
            return self.get_book_by_name(chapter_id)
        else:
            return {"message":"Chapter/Book Not Found"}
        
    
    def get_book_by_chapter_id(self, chapter_id):
        for book in self.all_book_list:
            for chapter in book.chapter_list:
                if chapter.chapter_id == chapter_id:
                    return book
        return "Book Not Found"
    
    def show_all_book_list(self):
        book_list=[]
        for book in self.all_book_list:
            book_list.append({"book_name": book.name,"pseudonym":book.pseudonym})
        return book_list
    
    # ____________________________________Add to list___________________________________

    def add_reader(self, reader):
        self.__reader_list.append(reader)
        
    def add_writer(self, writer):
        self.__writer_list.append(writer)
        
    def add_payment(self, payment):
        self.__payment_list.append(payment)

    def add_promotion(self, promotion):
        self.__promotion_list.append(promotion)
        
    # ____________________________________Check___________________________________
    
    def check_repeated_pseudonym(self, new_pseudonym):
        for pseudonym in self.all_pseudonym_list:
            if pseudonym.lower() == new_pseudonym.lower():
                return True
        return False
    
    def if_user_not_found(self, user):
        if not (isinstance(user, Reader) or isinstance(user, Writer)):
            return True
        return False
    
    def check_bought_chapter(self, username, chapter_id):
        user = self.get_user_by_username(username)
        if chapter_id in user.get_chapter_id_list():
            return True
        return False
    
    def check_user_role(self, username):
        user = self.get_user_by_username(username)
        if isinstance(user,Writer):
            return "writer"
        elif isinstance(user,Reader):
            return "reader"
        else:
            return "Not found user"
    
    
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> UI <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # ____________________________________Search___________________________________
        
    def search_all_list(self, search_str):
        search_book_list = self.search_book_by_name(search_str)
        search_pseudonym_list = self.search_pseudonym(search_str)

        search_dict = {"book": search_book_list,"pseudonym": search_pseudonym_list}
        return search_dict

    def search_book_by_name(self, book_name):
        search_list=[]
        for book in self.all_book_list:
            if book_name.lower() in book.name.lower():
                search_dict = {"book_name" : book.name,
                                "pseudonym": book.pseudonym,
                                "genre" : book.genre}
                search_list.append(search_dict)
        return search_list
    
    def search_pseudonym(self, pseudonym_str):
        search_list=[]
        for book in self.all_book_list:
            if pseudonym_str.lower() in book.pseudonym.lower():
                search_dict = {"book_name" : book.name,
                                "pseudonym": book.pseudonym,
                                "genre" : book.genre}
                search_list.append(search_dict)
        return search_list

    def search_user(self, username):
        search_reader_list = []
        search_writer_list = []
        for reader in self.__reader_list:
            if username.lower() in reader.username.lower():
                search_reader_list.append(reader.username)
        
        for writer in self.__writer_list:
            if username.lower() in writer.username.lower():
                search_writer_list.append(writer.username)

        # if search_reader_list == [] : search_reader_list = "Not Found"
        # if search_writer_list == [] : search_writer_list = "Not Found"
        
        return {"Reader" : search_reader_list, "Writer" : search_writer_list}
    
        
    def search_coin_promotion(self, code):
        if(code != None):
            for promotion in self.__promotion_list:
                if isinstance(promotion, CoinPromotion) and promotion.code == code:
                    return promotion  
        else: return None
        
    # ____________________________________Financials___________________________________
        
    def buy_coin(self, username, payment_method, payment_info, code, golden_amount):
        payment = self.create_payment_method(payment_method, payment_info)
        price = golden_amount
        silver_amount = int(golden_amount * 10 / 100)
        user = self.get_user_by_username(username)
        coin_promotion = self.search_coin_promotion(code)
        
        if(code != None and coin_promotion != None):
            print("Applying code")
            price = (100 - coin_promotion.discount) / 100 * price #ลดราคา 
        elif(coin_promotion != None):
                return "Your code is expired or not exist"
        else:
            print("Not applying any code")
            
        self.add_coin_to_user(user, payment, golden_amount, silver_amount, price)
        return "Purchase successful, THANK YOU"

    def add_coin_to_user(self, user, payment, golden_amount, silver_amount, price):
        payment.buy_coin(price)
        date_time = datetime.now()
        user.add_golden_coin(golden_amount)
        user.add_silver_coin(silver_amount)
        user.add_coin_transaction_list(CoinTransaction(payment.name, price, f"+{golden_amount}", f"+{silver_amount}", datetime.today()))
    
    def buy_chapter(self, username, chapter_id):
        user = self.get_user_by_username(username)
        if self.if_user_not_found(user): return user

        chapter = self.get_chapter_by_chapter_id(chapter_id)
        if not isinstance(chapter, Chapter): return chapter
        
        if user.check_repeated_purchase(chapter): return "already purchased"
        
        cost = chapter.cost

        coin_balance = user.user_coin_balance

        if coin_balance >= cost:
            user.deduct_coin(cost)
            user.add_chapter_transaction_list(ChapterTransaction(chapter, cost))
            return "Done"
        else:
            return "No coin"
    
    # ____________________________________Create / Add___________________________________

    def sign_up(self,username:str, password:str, birth_date: str, role:str):
        user = self.get_user_by_username(username)
        if not (role.lower() == "reader" or role.lower() == "writer"):
            return "please select Reader or Writer and try again"
        
        if not self.if_user_not_found(user): return "username is already taken"
        
        if role.lower() == "reader":
            self.add_reader(Reader(username, password, birth_date))
            
        elif role.lower() == "writer":
            self.add_writer(Writer(username, password, birth_date))
        
        return "Sign Up Successful"
    
    def create_book(self, name:str, pseudonym:str, writer_name:str, tag_list: str, status: str, age_restricted: bool, prologue: str):
        writer = self.get_user_by_username(writer_name)
        book = self.get_book_by_name(name)
        if isinstance(writer,Writer) and not isinstance(book,Book):
            new_book = Book(name, pseudonym, writer, tag_list, status,age_restricted, prologue)
            writer.add_writing_list(new_book)
            return {"create book successfully" : new_book.show_book_info(writer, self.__report_type_list)}
        return "please try again"
    
    #return reasons in detail, ไม่ควรสร้าง chapter ที่ n ได้ถ้ายังไม่มี n-1
    def create_chapter(self,book_name,chapter_number, name, context, cost):
        book = self.get_book_by_name(book_name)
        if isinstance(book,Book) and book.is_chapter_valid(chapter_number):
            chapter = Chapter(book_name, chapter_number, name, context, cost)
            book.add_chapter_list(chapter)
            return {"create Chapter successfully" : chapter.show_chapter_info()}
        else : 
            return "please try again"
        
    def create_comment(self, chapter_id, username, context):
        print(chapter_id,username,context)
        chapter = self.get_chapter_by_chapter_id(chapter_id)
        user = self.get_user_by_username(username)
        if isinstance(chapter, Chapter) and isinstance(user, Reader):
            new_comment = Comment(chapter, user, context)
            book = self.get_book_by_chapter_id(chapter_id)
            book.add_comment_list(new_comment)
            chapter.add_comment(new_comment)
            print("comment create")
            return new_comment.show_comment()
        else:
            print("No comment create")
            return {"Comment": "please try again"}
        
    def create_payment_method(self, payment_method_name, payment_info):
        if payment_method_name == self.__payment_list[0]:
            return OnlineBanking(payment_info)
        elif payment_method_name == self.__payment_list[1]:
            return DebitCard(payment_info)
        elif payment_method_name == self.__payment_list[2]:
            return TrueMoneyWallet(payment_info)
        
    def add_pseudonym(self, username, pseudonym):
        user = self.get_user_by_username(username)
        if self.if_user_not_found(user): return user
        if self.check_repeated_pseudonym(pseudonym):
            return "pseudonym already exists"
        user.add_pseudonym(pseudonym)
        return "pseudonym added"
    
    def create_report(self,book_name, username, report_type, context):
        user = self.get_user_by_username(username)
        book = self.get_book_by_name(book_name)
        if isinstance(book,Book) and isinstance(user,Reader) and report_type in self.report_type_list:
            new_report = Report(book,user,report_type, context)
            book.add_report_list(new_report)
            return {"massage":"report successfully"}
        else:
            return {"massage" : "! Cannot create report !"}
        
    def add_book_list(self,username,book_name):
        print("add book controller",book_name)
        user = self.get_user_by_username(username)
        book = self.get_book_by_name(book_name)
        return user.add_book_shelf_list(book)
        
    # ____________________________________Edit / Change___________________________________
            
    def edit_book_info(self, old_name, writer_name, new_name, genre, status, age_restricted, prologue):
        book = self.get_book_by_name(old_name)
        writer = self.get_user_by_username(writer_name)
        #เขียนดักไม่ให้ช้ำ
        if isinstance(book,Book):
            if writer == book.writer:
                if new_name:
                    book.name = new_name
                #เขียนดักให้เพิ่ม pseudonym ก่อนถึงจะใช้ได้ หรือ เพิ่ม pseudonym เข้าลิสต์หลังใช้ new_pseudonym
                if genre:
                    book.genre = genre
                if status:
                    book.status = status
                if age_restricted != book.age_restricted:
                    book.age_restricted = age_restricted
                if prologue:
                    book.prologue = prologue
                book.date_time = datetime.now() #last edit
                return {"Book updated" : book.show_book_info(writer, self.__report_type_list)}
        else:
            {"error" : "Book not found"}
            
    def edit_chapter_info(self,chapter_id, name, context, cost):
        chapter = self.get_chapter_by_chapter_id(chapter_id)
        if not isinstance(chapter, Chapter): return chapter
        if name:
            chapter.update_name(name)
        if context:
            chapter.update_context(context)
        if cost:
            chapter.update_cost(cost)
        # chapter.publish_date_time(0) #last edit
        return chapter.show_chapter_info()
    
    def change_password(self, username, old_password, new_password):
        user = self.get_user_by_username(username)
        if self.if_user_not_found(user): return user
        if user.password == old_password and len(new_password) >= 8:
            user.password = new_password
            return "Done"
        elif user.password != old_password:
            return "Wrong"
        elif len(new_password) < 8:
            return "Length"
        else:
            return "Error"
        
    def change_display_name(self, username, new_display_name):
        user = self.get_user_by_username(username)
        user.display_name = new_display_name
        return "display name has been changed"
    
    def edit_introducton(self, username, new_introduction):
        user = self.get_user_by_username(username)
        user.edit_introduction(new_introduction)
    
    # ____________________________________Show / View____________________________________
    
    def show_coin(self, username):
        user = self.get_user_by_username(username)
        if self.if_user_not_found(user): return user
        return {"golden_coin" : user.golden_coin.balance, "silver_coin" : user.silver_coin_balance}
    
    def show_my_page(self, username):
        user = self.get_user_by_username(username)
        if self.if_user_not_found(user): return user
        
        writing_count = "0"
        reads = "0"
        writing_list = [] # "Create your first writing"
        pseudonym_list = [] # "Pseudonym Not Found"
        comment_list = [] # "Add comment"
            
        if isinstance(user, Writer):
            writing_count = len(user.writing_list)
            reads = user.viewer_count
            writing_list = user.show_writing_name_list()
            pseudonym_list = user.pseudonym_list
            comment_list = user.show_comment_list()
        
        return {"display_name" : user.display_name,
                "username" : user.username,
                "introduction" : user.introduction,
                "writing_count" : writing_count,
                "book_on_shelf_count" : len(user.book_shelf_list),
                "followers" : len(user.follower_list),
                "read_count" : len(user.recent_read_chapter_list),
                "viewer_count" : reads,
                "writings" : writing_list,
                "pseudonyms" : pseudonym_list,
                "comments" : comment_list}
    
    def show_my_profile(self, username):
        user = self.get_user_by_username(username)
        if self.if_user_not_found(user): return user
        return {"display_name" : user.display_name,
                "username" : user.username}
        
        # "change password",
        #                     "go to page",
        #                     "upgrade to writer",
        #                     "pseudonym",
        #                     "verify age"
        
    def show_my_writing(self, username):
        user = self.get_user_by_username(username)
        if self.if_user_not_found(user): return user
        reading_list = []
        for book in user.writing_list:
            reading_list.append(book.show_book_info(user, self.__report_type_list))
        return reading_list
    
    def view_chapter(self, chapter_id):
        chapter = self.get_chapter_by_chapter_id(chapter_id)
        return chapter.show_chapter_info()
    
    def view_book(self, book_name, writer_name):
        book = self.get_book_by_name(book_name)
        writer = self.get_user_by_username(writer_name)
        if isinstance(book,Book):
            return book.show_book_info(writer, self.__report_type_list)
    
    def show_all_report(self,book_name):
        book = self.get_book_by_name(book_name)
        return book.show_report_list()
    
    def show_chapter_transaction(self, username):
        user = self.get_user_by_username(username)
        return user.show_chapter_transaction()
    
    def get_coin_transation(self, username):
        user = self.get_user_by_username(username)
        return user.show_coin_transaction()
    
    def get_silver_coin_list(self, username):
        user = self.get_user_by_username(username)
        return user.show_silver_coin_list()
    
    def show_book_shelf(self,username):
        user = self.get_user_by_username(username)
        return user.show_book_shelf(self.__report_type_list)
    
    def show_chapter_info(self,chapter_id):
        chapter = self.get_chapter_by_chapter_id_or_book(chapter_id)
        if isinstance(chapter, Chapter):
            return chapter.show_chapter_info()
        else:
            raise {"message" : "chapter not found"}
    
    def show_comment_list(self,chapter_id):
        chapter_or_book = self.get_chapter_by_chapter_id_or_book(chapter_id)
        if isinstance(chapter_or_book,Chapter) or isinstance(chapter_or_book,Book):
            return chapter_or_book.show_comment_list()
        else:
            return chapter_or_book
        
    def show_chapter_list_in_book(self,book_name):
        book = self.get_book_by_name(book_name)
        if isinstance(book,Book):
            return book.show_chapter_list()
        else:
            return {"message" : "Wrong book name"}

    # ____________________________________others___________________________________    
    
    def sign_in(self, username, password):
        user = self.get_user_by_username(username)
        if self.if_user_not_found(user): return "username doesn't exist"
        if user.password == password:
            if(isinstance(user, Reader)):
                return {"response" : "log in successfully", "role" : "reader"}
            if(isinstance(user, Writer)):
                return {"response" : "log in successfully", "role" : "writer"}
            
        return {"response" : "wrong password"}