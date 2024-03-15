from datetime import datetime

class Report:
    def __init__(self, book, user, report_type, context):
        self.__book = book
        self.__user = user
        self.__report_type = report_type
        self.__context = context
        self.__date_time = datetime.now()

    @property
    def book(self):
        return self.__book
    @property
    def user(self):
        return self.__user
    @property
    def report_type(self):
        return self.__report_type
    @property
    def context(self):
        return self.__context
    @property
    def date_time(self):
        return f"{self.__date_time.strftime("%x")} {self.__date_time.strftime("%X")}"

    @user.setter
    def user(self,user):
        self.__user = user
        return self.__user

    @report_type.setter
    def report_type(self,report_type):
        self.__report_type = report_type
        return self.__report_type

    @context.setter
    def context(self,context):
        self.__context = context
        return self.__context

    @date_time.setter
    def date_time(self,date_time):
        self.__date_time = date_time.now()

    def delete(self):
        self.__report_to.delete_report(self)
        
    def show_report(self):
        return {"book_name" : self.book.name,
                "user" : self.user.username,
                "report_type" : self.report_type,
                "date_time" : self.date_time,
                "context" : self.context}