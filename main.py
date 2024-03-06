from typing import Union
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
from datetime import datetime, timedelta

from Controller import Controller
from Reader import Reader, Writer
from Book import Book
from Chapter import Chapter
from Payment import Payment, OnlineBanking, TrueMoneyWallet
from CoinTransaction import CoinTransaction
from Promotion import BookPromotion, CoinPromotion, Promotion
from Coin import GoldenCoin, SilverCoin

app = FastAPI()

write_a_read = Controller()

if __name__ == "__main__":
     uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")

now = datetime.now()

#uvicorn main:app --reload

#----------------------------------create users----------------------------------
#WriteARead.add_reader(Reader("username", "password", "dd/mm/yyyy"))
     
Mo = Writer("Mozaza", "12345678", "12/05/2000")
write_a_read.add_reader(Mo)
write_a_read.add_reader(Reader("Pinttttt", "sawasdee", "01/01/2005"))
write_a_read.add_reader(Reader("Pangrum", "ehehe", "02/01/2005"))
write_a_read.add_reader(Reader("Jueeen", "whippedcream", "12/11/2004"))

write_a_read.add_writer(Mo)

#----------------------------------create books----------------------------------
# Book("name", writer, [tag_list], "publishing/hiding", age_restricted, "prologue", "dd/mm/yyyy"):

shin_chan_prologue = "Shin Chan is a 50-year-old boy"

Book1 = Book("Shin_chan", Mo, ["kids", "comedy","crime"], "publishing", 7, shin_chan_prologue)
Mo.add_writing_book_list(Book1)

Book2 = Book("Shinosuke", Mo, ["kids", "comedy","crime"], "publishing", 7, shin_chan_prologue)
Mo.add_writing_book_list(Book2)


#----------------------------------create chapters----------------------------------
#Chapter("number", "name", "context", "dd/mm/yyyy", price)

Book1.add_chapter_list(Chapter("1", "first_ch", "this is the first chapter of shincha", 184, "Shin_chan"))

#----------------------------------create promotions----------------------------------
#BookPromotion("dd/mm/yyyy", discount, [book_list])
#CoinPromotion("dd/mm/yyyy", discount, "code")


book_sale = BookPromotion("01/01/2021",50, [])
write_a_read.add_promotion(book_sale)

free_coin = CoinPromotion("01/01/2021",40, "chakeawaroi")
write_a_read.add_promotion(free_coin)

#----------------------------------create transactions----------------------------------

Mo.add_coin_transaction_list(CoinTransaction(OnlineBanking("012-3-45678-9"), 100, 100, 10, now))
Mo.add_coin_transaction_list(CoinTransaction(TrueMoneyWallet("0123456789", "5174"), 200, 200, 20, now))

#----------------------------------add coin----------------------------------
Mo.add_silver_coin(20)
Mo.add_silver_coin(10)
Mo.add_silver_coin(50)
Mo.add_silver_coin(3)
Mo.add_silver_coin(100)
Mo.add_golden_coin(888)

#----------------------------------add to bookshelf----------------------------------
Mo.add_book_shelf_list(Book1)
Mo.add_book_shelf_list(Book2)
#----------------------------------fastapi----------------------------------

@app.get("/")
def FirstPage():
     return "Welcome to WriteARead"

@app.get("/bookname", tags=['search bar'])
def searchBook(book_name:str):
     return {"Book": write_a_read.search_book_by_name(book_name)}

@app.get("/username", tags=['search bar'])
def SearchUser(username:str):
     return {"user": write_a_read.search_user(username)}

@app.get("/coin", tags=['coin'])
def ShowCoins(username:str):
     return write_a_read.show_coin(username)

@app.get("/silver_coin", tags=['coin'])
def ShowSilverCoins(username:str):
     user = write_a_read.get_user_by_username(username)
     return {"Silver_Coin" :user.show_silver_coin_list()}

@app.post("/sign_up", tags=['sign up/sign in'])
def SignUp(username:str, password:str, birth_date: str):
     return write_a_read.sign_up(username, password, birth_date)

@app.get("/my_page", tags=['user'])
def ShowMyPage(username:str):
     return {"My Page" : write_a_read.show_my_page(username)}

class dto_edit_introduction(BaseModel):
     username : str
     text : str
     
@app.put("/my_page/edit_introduction", tags=["user"])
def EditIntroduction(dto : dto_edit_introduction):
     user = write_a_read.get_user_by_username(dto.username)
     return {"Edit Introduction" : user.edit_introduction(dto.text)}


@app.get("/my_profile", tags=['user'])
def ShowMyProfile(username:str):
     return {"My Profile" : write_a_read.show_my_profile(username)}

@app.get("/get_coin_transaction", tags=['Coin Transaction'])
def get_coin_transaction(username:str):
     user = write_a_read.get_user_by_username(username)
     return {"Coin Transaction" : user.show_coin_transaction()}

@app.get("/show_chapter_transaction", tags=['Chapter Transaction'])
def ShowChapterTransaction(username:str):
     user = write_a_read.get_user_by_username(username)
     if write_a_read.if_user_not_found(user): return user
     return {"Chapter Transaction" : user.show_chapter_transaction()}

class dto_change_password(BaseModel):
     username : str
     old_password :str
     new_password : str
     
@app.put("/my_profile/change_password", tags=['user'])
def ChangePassword(dto : dto_change_password):
     return {"Change Password" : write_a_read.change_password(dto.username, dto.old_password, dto.new_password)}

class dto_change_display_name(BaseModel):
     username : str
     new_display_name : str
     
@app.put("/my_page/change_display_name", tags=['user'])
def ChangeDisplayName(dto : dto_change_display_name):
     return {"Change Display Name" : write_a_read.change_display_name(dto.username, dto.new_display_name)}

class dto_add_pseudonym(BaseModel):
     username : str
     new_pseudonym : str
     
@app.post("/my_profile/psedonym", tags=["user"])
def AddPseudonym(dto : dto_add_pseudonym):
     return {"Add Pseudonym" : write_a_read.add_pseudonym(dto.username, dto.new_pseudonym)}

@app.get("/my_reading", tags=['user'])
def ShowMyReading(username:str):
     return {"My Reading" : write_a_read.show_my_reading(username)}

class dto_buy_chapter(BaseModel):
     username : str
     chapter_id : str
     
@app.post("/buy_chapter", tags=['chapter'])
def BuyChapter(dto : dto_buy_chapter):
     return {"Buy Chapter" : write_a_read.buy_chapter(dto.username, dto.chapter_id)}

@app.get("/test", tags=['test'])
def Test(book_name:str):
     return {write_a_read.get_book_by_name(book_name)}
#----------------------------------test----------------------------------

# print(ShowMyReading("Mozaza"))
# test0 = WriteARead.show_coin("Mozaza")
# test = Mo.show_silver_coin_list()
# test1 = WriteARead.buy_chapter("Mozaza", "first chapter of shinchan/1")
# test2 = WriteARead.show_coin("Mozaza")
# test3 = Mo.show_silver_coin_list()

# print(test0)
# print(test)
# print(test1)
# print(test2)
# print(test3)

# print(Mo.show_chapter_transaction())

# print(f"{Mo.get_coin_transaction_list()[2].golden_amount} , {Mo.get_coin_transaction_list()[2].silver_amount}")

# print("\n\n\n")

# print(Mo.show_silver_coin_list())
# for silver_coin in Mo.get_silver_coin_list():
#      print((silver_coin.balance))

# print(Mo.show_silver_coin_list())
# for silver_coin in Mo.get_silver_coin_list():
#      print((silver_coin.balance))
