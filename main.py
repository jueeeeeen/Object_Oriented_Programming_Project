from typing import Optional
import uvicorn
from fastapi import FastAPI, Query, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from datetime import datetime 
from Controller import Controller
from Reader import Reader, Writer
from Book import Book
from Payment import OnlineBanking, TrueMoneyWallet
from CoinTransaction import CoinTransaction
from Promotion import CoinPromotion



# origins = [
#      "http://localhost:5500",
#      "localhost:5500",
#      "http://127.0.0.1:5500",
#      "127.0.0.1:5500/",
#      "http://localhost:8000",
#      "localhost:8000",
#      "http://127.0.0.1:8000",
#      "127.0.0.1:8000/"
# ]


app = FastAPI()
# app.add_middleware(
#      CORSMiddleware,
#      allow_origins=origins,
#      allow_credentials=True,
#      allow_methods=["*"],
#      allow_headers=["*"]
# )

templates = Jinja2Templates(directory="Templates")
app.mount("/Templates", StaticFiles(directory="Templates"), name="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/scripts", StaticFiles(directory="scripts"), name="scripts")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")


write_a_read = Controller()

if __name__ == "__main__":
     uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")

#user
Mo = Writer("Mozaza", "12345678", "12/05/2000")
Jin = Writer("Jinzaza", "12345678", "01/01/2005")
Pint = Reader("Pintzaza", "12345678", "01/01/2005")
Pang = Reader("Pangzaza", "12345678", "01/01/2004")
#add user
write_a_read.add_writer(Mo)
write_a_read.add_writer(Jin)
write_a_read.add_reader(Pint)
write_a_read.add_reader(Pang)

#prologue
shin_chan_prologue = "Shin Chan is a 50-year-old boy"
doraemon_prologue = "Doraemon, Noby, and their three friends are sucked into a portal during a heavy storm and transported to the village of Natura. It becomes apparent that the gadgets Doraemon usually carries, that could potentially save them and return them to the present, are all missing."
sailor_moon_prologue = "A 14-year-old underachieving young schoolgirl named Usagi Tsukino meets a magical talking cat named Luna. Luna gives Usagi the ability to transform into a magical alter ego — Sailor Moon — tasked with locating the moon princess and battling the evil forces of the Dark Kingdom."
orv_prologue = "A novel called Three Ways to Survive in a Ruined World (written by the anonymous author tls123) has been written and published over the course of a decade, and Kim Dokja is the sole reader who has followed it to its ending. When the real world is plunged into the premise of Ways of Survival, Kim Dokja's unique knowledge of the novel becomes vital to his survival."
naruto_prologue = "A powerful fox known as the Nine-Tails attacks Konoha, the hidden leaf village in the Land of Fire, one of the Five Great Shinobi Countries in the Ninja World. In response, the leader of Konoha and the Fourth Hokage, Minato Namikaze, at the cost of his life, seals the fox inside the body of his newborn son, Naruto Uzumaki, making him a host of the beast."

#book
write_a_read.create_book("Shin chan", "Mola", "Mozaza", "adventure", "publishing", False, shin_chan_prologue) #1
write_a_read.create_book("Shinnosuke", "Mola", "Mozaza", "comedy", "publishing", True, shin_chan_prologue) #2
write_a_read.create_book("Doraemon", "Jina", "Jinzaza", "comedy", "publishing", False, doraemon_prologue) #3
write_a_read.create_book("Doraemon Special", "Jina", "Jinzaza", "adventure", "publishing", False, doraemon_prologue) #4
write_a_read.create_book("Sailor moon", "Jinny", "Jinzaza", "fantasy", "publishing", True, sailor_moon_prologue) #5
write_a_read.create_book("Sailor moon Special", "Jinny", "Jinzaza", "fantasy", "publishing", False, sailor_moon_prologue) #6
write_a_read.create_book("Omniscient readers viewpoint", "MolaMola", "Mozaza", "sci-fi", "publishing", True, orv_prologue) #7
write_a_read.create_book("Omniscient readers viewpoint Special", "MolaMola", "Mozaza", "sci-fi", "publishing", False, orv_prologue) #8
write_a_read.create_book("Naruto", "Moeiei", "Mozaza", "adventure", "publishing", False, naruto_prologue) #9
write_a_read.create_book("Naruto Special", "Moeiei", "Mozaza", "adventure", "publishing", False, naruto_prologue) #10

shin_chan_chapter_1 = "While playing at the local park, Shinnosuke & his 4 friends Kazama, Nene, Masao & Bo encounter an woman named Tamiko, who claims to be Shinnosuke's would-be-wife from future. She states that in 20 years into the future Shinnosuke had been converted into a stone statue by Tamiko's father, but before being converted into stone, Shinnosuke asked Tamiko to bring his 5 year old self. Tamiko takes the five 5-year old children into the future via a time machine in order to save the adult Shinnosuke. After reaching the future, Tamiko is ambushed by the men employed by his father Masuzo Kaneari, who took her back to her house. The children seek refuge at the Shinnosuke's house. Here they meet Shinnosuke's parents Hiroshi & Misae.\n To Be continue...\n please buy next chapter"

# chap
write_a_read.create_chapter("Shin chan", "1", "Shin chan first ch", shin_chan_chapter_1, 184)
write_a_read.create_chapter("Shin chan", "2", "Shin chan second ch", "this is the second chapter of shincha", 200)
write_a_read.create_chapter("Shin chan", "3", "Shin chan third ch", "this is the third chapter of shincha", 300)
write_a_read.create_chapter("Shinnosuke", "1", "Shinnosuke first ch", "this is the first chapter of shincha", 184)
write_a_read.create_chapter("Doraemon", "1", "Doraemon first ch", "this is the first chapter of Doraemon", 0)
write_a_read.create_chapter("Doraemon Special", "1", "Doraemon Special first ch", "this is the first chapter of Doraemon Special", 500)
write_a_read.create_chapter("Doraemon Special", "2", "Doraemon Special second ch", "this is the second chapter of Doraemon Special", 500)
write_a_read.create_chapter("Sailor moon", "1", "Sailor moon first ch", "this is the first chapter of Sailor moon", 0)
write_a_read.create_chapter("Sailor moon Special", "1", "Sailor moon Special first ch", "this is the first chapter of Sailor moon Special", 40)
write_a_read.create_chapter("Omniscient readers viewpoint", "1", "Omniscient readers first ch", "this is the first chapter of Omniscient readers", 0)
write_a_read.create_chapter("Omniscient readers viewpoint Special", "1", "Omniscient readers Special first ch", "this is the first chapter of Omniscient readers Special", 750)
write_a_read.create_chapter("Naruto", "1", "Naruto first ch", "this is the first chapter of Naruto", 0)
write_a_read.create_chapter("Naruto Special", "1", "Naruto Special first ch", "this is the first chapter of Naruto Special", 800)

write_a_read.create_comment("Shin chan-1", "Pangzaza", "wow very fun! I love your writing.")
write_a_read.create_comment("Shin chan-1", "Pintzaza", "I love your writing. Saranghae Mola!!!")
write_a_read.create_comment("Shinnosuke-1", "Pangzaza", "why so expensive. :(")

write_a_read.buy_coin("Mozaza","OnlineBanking","1",None, 999999999999)

#promotion
promotion_11_11 = CoinPromotion("15/03/2024", 10, "November")
promotion_12_12 = CoinPromotion("15/03/2024", 20, "December")
write_a_read.add_promotion(promotion_11_11)
write_a_read.add_promotion(promotion_12_12)

#add coin transac
Mo.add_coin_transaction_list(CoinTransaction(OnlineBanking("0123456789"), 500, "+500", "+50", "20/02/2024, 15:23:10"))
Mo.add_coin_transaction_list(CoinTransaction(TrueMoneyWallet("0989899889"), 500, "+500", "+50", "20/02/2024, 15:23:10"))
# ____________________________________FastAPI___________________________________
# _________________________________________________ GET _________________________________________________

@app.get("/")
def first_page(req: Request):
     return templates.TemplateResponse(name="sign_in.html", context={"request":req})

@app.get("/show_all_book")
def show_all_book():
     return write_a_read.show_all_book_list()

@app.get("/book/{book_name}")
async def get_book_info(book_name: str, writer_name: str):
     return write_a_read.view_book(book_name, writer_name)
     
@app.get("/chapter/comment/{chapter_id}", tags=['chapter'])
def show_comment_list(chapter_id:str):
     return write_a_read.show_comment_list(chapter_id)

@app.get("/chapter/info/{chapter_id}")
async def get_chapter_info(chapter_id: str):
     return write_a_read.show_chapter_info(chapter_id)
     
@app.get("/book/chapter/{book_name}", tags=['book'])
def show_chapter_list(book_name:str):
     return write_a_read.show_chapter_list_in_book(book_name)

@app.get("/bookname", tags=['search bar'])
def search_book(book_name:str):
     return {"Book": write_a_read.search_book_by_name(book_name)}

@app.get("/coin/{username}", tags=['coin'])
def my_coin(username:str):
     return write_a_read.show_coin(username)

@app.get("/my_page/{username}", tags=['My Page'])
def show_my_page(username:str):
     return write_a_read.show_my_page(username)

@app.get("/my_profile/{username}", tags=['My Profile'])
def show_my_profile(username:str):
     return write_a_read.show_my_profile(username)

@app.get("/my_writing/{username}", tags=['My Writing'])
def show_my_writing(username:str):
     return write_a_read.show_my_writing(username)

@app.get("/get_coin_transaction/{username}", tags=['Coin Transaction'])
def get_coin_transaction(username:str):
     return write_a_read.get_coin_transation(username)

@app.get("/show_chapter_transaction/{username}", tags=['Chapter Transaction'])
def show_chapter_transaction(username:str):
     return write_a_read.show_chapter_transaction(username)

@app.get("/sign_in", tags=['sign up/sign in'])
def sign_in(username:str, password:str):
     return write_a_read.sign_in(username, password)

@app.get("/search_all/{search_str}", tags=['search bar'])
def search_all(search_str:str):
     return write_a_read.search_all_list(search_str)

@app.get("/check_bought_chapter/{username}", tags=['check'])
def check_bought_chapter(username:str, chapter_id:str):
     return write_a_read.check_bought_chapter(username, chapter_id)

@app.get("/check_writer/{username}")
def check_writer(username:str):
     return {"role": write_a_read.check_user_role(username)}

#......................................................No frontend....................................................

@app.get("/report/{book_name}" )
def show_all_report(book_name:str):
     return write_a_read.show_all_report(book_name)

@app.get("/my_reading", tags=['My Reading'])
def show_my_reading(username:str):
     return write_a_read.show_my_reading(username)

@app.get("/silver_coin", tags=['coin'])
def show_silver_coin(username:str):
     return write_a_read.get_silver_coin_list(username)

@app.get("/book_shelf")
def show_book_shelf(username:str):
     return write_a_read.show_book_shelf(username)

# _________________________________________________ POST _________________________________________________

# #..................................................has frontend........................................................


class dto_create_report(BaseModel):
     book_name:str
     username:str
     report_type:str
     context: str
     
@app.post("/report/{book_name}", tags=['report'])
def create_report(dto : dto_create_report):
     return write_a_read.create_report(dto.book_name, dto.username, dto.report_type, dto.context)
     
#..........................................................................................................

class dto_sign_up(BaseModel):
     username:str
     password:str
     birth_date: str
     role: str

@app.post("/sign_up", tags=['sign up/sign in'])
def sign_up(dto : dto_sign_up):
     return write_a_read.sign_up(dto.username, dto.password, dto.birth_date, dto.role)

# #...........................................................................................................


class dto_buy_chapter(BaseModel):
     username : str
     chapter_id : str

@app.post("/buy_chapter/{username}", tags=['chapter'])
def buy_chapter(dto : dto_buy_chapter):
     return write_a_read.buy_chapter(dto.username, dto.chapter_id)

#..........................................................................................................

class dto_create_book(BaseModel):
     name:str
     writer_name:str
     genre: str
     prologue: str
     age_restricted: bool
     status: str 
     pseudonym: str
     
@app.post("/book", tags=['Book'])
def create_book(dto : dto_create_book):
     return write_a_read.create_book(dto.name, dto.pseudonym, dto.writer_name, dto.genre, dto.status, dto.age_restricted, dto.prologue)
#..........................................................................................................

class dto_create_chapter(BaseModel):
     book_name:str
     chapter_number:int
     name:str
     context: str
     cost : int
     
@app.post("/chapter", tags=['Chapter'])
def create_chapter(dto : dto_create_chapter):
     return write_a_read.create_chapter(dto.book_name, dto.chapter_number, dto.name, dto.context, dto.cost)

#..........................................................................................................

class dto_create_comment(BaseModel):
     chapter_id : str
     username : str
     context : str
     
@app.post("/comment/{chapter_id}", tags=['Comment'])
def create_comment(dto: dto_create_comment):
     return write_a_read.create_comment(dto.chapter_id, dto.username, dto.context)
     
#..........................................................................................................

class dto_buy_coin(BaseModel):
     username : str
     golden_coin_amount : int
     payment_method : str 
     payment_info : str
     code: Optional[str] = None

@app.post("/buy_coin", tags=['Buy Coin'])
def buy_coin(dto : dto_buy_coin):
     return write_a_read.buy_coin(dto.username, dto.payment_method, dto.payment_info, dto.code, dto.golden_coin_amount)
#......................................................No frontend....................................................

class dto_add_pseudonym(BaseModel):
     username : str
     new_pseudonym : str

@app.post("/my_profile/psedonym", tags=["My Profile"])
def add_pseudonym(dto : dto_add_pseudonym):
     return write_a_read.add_pseudonym(dto.username, dto.new_pseudonym)

# _________________________________________________ PUT _________________________________________________

# #..................................................has frontend........................................................

class dto_change_password(BaseModel):
     username : str
     old_password :str
     new_password : str

@app.put("/change_password/{username}", tags=['My Profile'])
def change_password(dto: dto_change_password):
     return write_a_read.change_password(dto.username, dto.old_password, dto.new_password)

#........................................................................................................................

class dto_edit_book(BaseModel):
     old_name : str = None
     writer_name : str = None
     new_name : str = None
     new_genre: str = None
     prologue: str = None
     age_restricted: bool = None
     status: str = None
     
@app.put("/edit_book", tags=['Book'])
def edit_book_info(dto : dto_edit_book):
     return write_a_read.edit_book_info(dto.old_name, dto.writer_name, dto.new_name, dto.new_genre, dto.status, dto.age_restricted, dto.prologue)

#......................................................No frontend....................................................

class dto_add_book_shelf(BaseModel):
     username : str
     book_name :str

@app.put("/book_shelf/add")
def add_book_shelf(dto : dto_add_book_shelf):
     return {"book shelf" : write_a_read.add_book_list(dto.username, dto.book_name)}
     
#........................................................................................................................

class dto_edit_chapter(BaseModel):
     chapter_id : str = None
     name : str = None
     context : str = None
     cost : int = None
     
@app.put("/edit_chapter", tags=['Chapter'])
def edit_chapter_info(dto : dto_edit_chapter):
     return write_a_read.edit_chapter_info(dto.chapter_id, dto.name, dto.context, dto.cost)

#.....................................................No frontend.....................................................

class dto_change_display_name(BaseModel):
     username : str
     new_display_name : str

@app.put("/my_page/change_display_name", tags=['My Page'])
def change_display_name(dto : dto_change_display_name):
     return {"Change Display Name" : write_a_read.change_display_name(dto.username, dto.new_display_name)}

#........................................................................................................................

class dto_edit_introduction(BaseModel):
     username : str
     text : str

@app.put("/my_page/edit_introduction", tags=["My Page"])
def edit_introduction(dto : dto_edit_introduction):
     return write_a_read.edit_introduction(dto.username, dto.text)

@app.delete('/report/delete/', tags=['Report'])
async def delete_report(book_name: str, report_type : str):
   return write_a_read.delete_report(book_name,report_type)