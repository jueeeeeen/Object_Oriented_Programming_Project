from datetime import datetime, timedelta

class Webmaster:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    @property
    def username(self):
        return self.username
    @property
    def password(self):
        return self.password
    
    @username.setter
    def username(self,username):
        self.__username = username
        return self.__username
    @password.setter
    def password(self,password):
        self.__password = password
        return self.__password

    def check_edits(self, book):
        if book.edited and (datetime.now() - book.counting_date_time).days <= 7:
            return True
        return False
      