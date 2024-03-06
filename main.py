from typing import Union
import uvicorn
from fastapi import FastAPI
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

WriteARead = Controller()

if __name__ == "__main__":
     uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")

now = datetime.now()

#uvicorn main:app --reload

#----------------------------------create users----------------------------------
#WriteARead.add_reader(Reader("username", "password", "dd/mm/yyyy"))
     
Mo = Writer("Mozaza", "namchakeawpun", "12/05/2000")
WriteARead.add_reader(Mo)
WriteARead.add_reader(Reader("Pinttttt", "sawasdee", "01/01/2005"))
WriteARead.add_reader(Reader("Pangrum", "ehehe", "02/01/2005"))
WriteARead.add_reader(Reader("Jueeen", "whippedcream", "12/11/2004"))

WriteARead.add_writer(Mo)

#----------------------------------create books----------------------------------
# Book("name", writer, [tag_list], "publishing/hiding", age_restricted, "prologue", "dd/mm/yyyy"):

shin_chan_prologue = "Shin Chan is a 50-year-old boy"

Book1 = Book("Shin_chan", Mo, ["kids", "comedy","crime"], "publishing", 7, shin_chan_prologue)
Mo.add_writing_book_list(Book1)

Book2 = Book("Shinosuke", Mo, ["kids", "comedy","crime"], "publishing", 7, shin_chan_prologue)
Mo.add_writing_book_list(Book2)


#----------------------------------create chapters----------------------------------
#Chapter("number", "name", "context", "dd/mm/yyyy", price)

Chapter1_1 = Chapter("1", "first chapter of shinchan", "this is the first chapter of shincha", 100)
Book1.add_chapter_list(Chapter1_1)

#----------------------------------create promotions----------------------------------
#BookPromotion("dd/mm/yyyy", discount, [book_list])
#CoinPromotion("dd/mm/yyyy", discount, "code")


book_sale = BookPromotion("01/01/2021",50, [])
WriteARead.add_promotion(book_sale)

free_coin = CoinPromotion("01/01/2021",40, "chakeawaroi")
WriteARead.add_promotion(free_coin)

#----------------------------------create transactions----------------------------------

Mo.add_coin_transaction_list(CoinTransaction(OnlineBanking("012-3-45678-9"), 100, [100, 10], now.strftime("%d/%m/%Y, %H:%M:%S")))
Mo.add_coin_transaction_list(CoinTransaction(TrueMoneyWallet("0123456789", "5174"), 200, [200, 20], now.strftime("%d/%m/%Y, %H:%M:%S")))

#----------------------------------add coin----------------------------------
Mo.add_silver_coin(20)
Mo.add_silver_coin(50)
Mo.add_silver_coin(100)
Mo.add_golden_coin(2)
#----------------------------------fastapi----------------------------------

@app.get("/")
def FirstPage():
     return "Welcome to WriteARead"

@app.get("/bookname", tags=['search bar'])
def searchBook(book_name:str):
    return {"Book": WriteARead.search_book_by_name(book_name)}

@app.get("/username", tags=['search bar'])
def SearchUser(username:str):
     return {"user": WriteARead.search_user(username)}

@app.get("/coin", tags=['coin'])
def ShowCoins(username:str):
     return WriteARead.show_coin(username)

@app.get("/silver_coin", tags=['coin'])
def ShowSilverCoins(username:str):
     user = WriteARead.get_user_by_username(username)
     return {"Silver_Coin" :user.show_silver_coin_list()}

@app.post("/signup", tags=['sign up/sign in'])
def SignUp(username:str, password:str, birth_date: str):
    return WriteARead.sign_up(username, password, birth_date)

@app.get("/My Page", tags=['user'])
def ShowMyPage(username:str):
     return {"My Page" : WriteARead.show_my_page(username)}

@app.get("/My Profile", tags=['user'])
def ShowMyProfile(username:str):
     return {"My Profile" : WriteARead.show_my_profile(username)}

@app.get("/get_coin_transacttion", tags=['Coin Transaction'])
def get_coin_transaction(username:str):
    user = WriteARead.get_user_by_username(username)
    return {"Coin Transaction" : user.show_coin_transaction()}

@app.put("/My Profile/change_password", tags=['user'])
def ChangePassword(username:str, new_password:str):
     return {"Change Password" : WriteARead.change_password(username, new_password)}

@app.post("/My Profile/psedonym", tags=["user"])
def AddPseudonym(username:str, new_pseudonym:str):
     return {"Add Pseudonym" : WriteARead.add_pseudonym(username, new_pseudonym)}

@app.get("/My Reading", tags=['user'])
def ShowMyReading(username:str):
     return {"My Reading" : WriteARead.show_my_reading(username)}

@app.get("/Buy Chapter", tags=['chapter'])
def BuyChapter(username:str, chapter_id:str):
     return {"Buy Chapter" : WriteARead.buy_chapter(username)}
#----------------------------------test----------------------------------
test = Mo.show_silver_coin_list()
test1 = WriteARead.buy_chapter("Mozaza", "first chapter of shinchan/1")
test2 = WriteARead.show_coin("Mozaza")
test3 = Mo.show_silver_coin_list()
print(test)
print(test1)
print(test2)
print(test3)
