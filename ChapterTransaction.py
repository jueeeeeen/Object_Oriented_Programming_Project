from datetime import datetime

class ChapterTransaction:
  def __init__(self,chapter, price):
      self.__chapter = chapter
      self.__price = price
      self.__date_time = datetime.now()
      
  @property
  def chapter(self):
    return self.__chapter

  @property
  def price(self):
    return self.__price

  @property
  def date_time(self):
    return self.__date_time

  @property
  def date_time_str(self):
    return self.__date_time.strftime("%x %X")

  def chapter_transaction(self):
    return f"chapter : {self.chapter.name} | price : {self.__price} | date time : {self.date_time_str}"

  def chapter_transaction_json(self):
    return {"chapter" : self.chapter.name,
            "price" : self.__price,
            "date_time" : self.date_time_str}
    
