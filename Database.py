from Book import Book
from Chapter import Chapter
from Payment import TrueMoneyWallet, OnlineBanking, DebitCard, PaymentMethod
from Promotion import CoinPromotion, BookPromotion
from Reader import Reader, Writer
from Controller import Controller
from CoinTransaction import CoinTransaction
from ChapterTransaction import ChapterTransaction

from datetime import datetime, date, timedelta

write_a_read = Controller()

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
write_a_read.create_book("Shin_chan", "Mola", "Mozaza", "adventure", "publishing", False, shin_chan_prologue) #1
write_a_read.create_book("Shinosuke", "Mola", "Mozaza", "comedy", "publishing", True, shin_chan_prologue) #2
write_a_read.create_book("Doraemon", "Jina", "Jinzaza", "comedy", "publishing", False, doraemon_prologue) #3
write_a_read.create_book("Doraemon_Special", "Jina", "Jinzaza", "adventure", "publishing", False, doraemon_prologue) #4
write_a_read.create_book("Sailor_moon", "Jinny", "Jinzaza", "fantasy", "publishing", True, sailor_moon_prologue) #5
write_a_read.create_book("Sailor_moon_Special", "Jinny", "Jinzaza", "fantasy", "publishing", False, sailor_moon_prologue) #6
write_a_read.create_book("Omniscient_readers_viewpoint", "MolaMola", "Mozaza", "sci-fi", "publishing", True, orv_prologue) #7
write_a_read.create_book("Omniscient_readers_viewpoint_Special", "MolaMola", "Mozaza", "sci-fi", "publishing", False, orv_prologue) #8
write_a_read.create_book("Naruto", "Moeiei", "Mozaza", "adventure", "publishing", False, naruto_prologue) #9
write_a_read.create_book("Naruto_Special", "Moeiei", "Mozaza", "adventure", "publishing", False, naruto_prologue) #10

# chap
write_a_read.create_chapter("Shin_chan", "1", "Shin_chan_first_ch", "this is the first chapter of shincha", 184)
write_a_read.create_chapter("Shin_chan", "2", "Shin_chan_second_ch", "this is the second chapter of shincha", 200)
write_a_read.create_chapter("Shin_chan", "3", "Shin_chan_third_ch", "this is the third chapter of shincha", 300)
write_a_read.create_chapter("Shinosuke", "1", "Shinosuke_first_ch", "this is the first chapter of shincha", 184)
write_a_read.create_chapter("Doraemon", "1", "Doraemon_first_ch", "this is the first chapter of Doraemon", 0)
write_a_read.create_chapter("Doraemon_Special", "1", "Doraemon_Special_first_ch", "this is the first chapter of Doraemon_Special", 500)
write_a_read.create_chapter("Doraemon_Special", "2", "Doraemon_Special_second_ch", "this is the second chapter of Doraemon_Special", 500)
write_a_read.create_chapter("Sailor_moon", "1", "Sailor_moon_first_ch", "this is the first chapter of Sailor_moon", 0)
write_a_read.create_chapter("Sailor_moon_Special", "1", "Sailor_moon_Special_first_ch", "this is the first chapter of Sailor_moon_Special", 40)
write_a_read.create_chapter("Omniscient_readers_viewpoint", "1", "Omniscient_readers_viewpoint_first_ch", "this is the first chapter of Omniscient_readers_viewpoint", 0)
write_a_read.create_chapter("Omniscient_readers_viewpoint_Special", "1", "Omniscient_readers_viewpoint_Special_first_ch", "this is the first chapter of Omniscient_readers_viewpoint_Special", 750)
write_a_read.create_chapter("Naruto", "1", "Naruto_first_ch", "this is the first chapter of Naruto", 0)
write_a_read.create_chapter("Naruto_Special", "1", "Naruto_Special_first_ch", "this is the first chapter of Naruto_Special", 800)

write_a_read.create_comment("Shin_chan-1", "Pangzaza", "wow very fun! I love your writing.")
write_a_read.create_comment("Shin_chan-1", "Pintzaza", "I love your writing. Saranghae Mola!!!")
write_a_read.create_comment("Shinosuke-1", "Pangzaza", "why so expensive. :(")


#promotion
promotion_11_11 = CoinPromotion("15/03/2024", 10, "November")
promotion_12_12 = CoinPromotion("15/03/2024", 20, "December")
write_a_read.add_promotion(promotion_11_11)
write_a_read.add_promotion(promotion_12_12)

book_for_promotion = Book("Promotoin", "Molapro", "Mozaza", "promo_only", "publishing", False, "Promotoin testttttttt")
write_a_read.add_promotion(BookPromotion("15/03/2024", 10, [book_for_promotion]))

#add coin transac
Mo.add_coin_transaction_list(CoinTransaction(OnlineBanking("0123456789"), 500, "+500", "+50", "20/02/2024, 15:23:10"))
Mo.add_coin_transaction_list(CoinTransaction(TrueMoneyWallet("0989899889"), 500, "+500", "+50", "20/02/2024, 15:23:10"))