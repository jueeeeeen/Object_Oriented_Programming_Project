from Chapter import Chapter
from Report import Report #
from Comment import Comment #
from datetime import datetime, timedelta

class Book:
    def __init__(self, name, pseudonym, writer, genre, status, age_restricted, prologue):
        self.__name = name
        self.__pseudonym = pseudonym
        self.__writer = writer
        self.__genre = genre
        self.__status = status
        self.__age_restricted = age_restricted
        self.__prologue = prologue
        self.__chapter_list = []
        self.__comment_list = []
        self.__report_list = []
        self.__date_time = datetime.now()
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
        
    @property
    def pseudonym(self):
        return self.__pseudonym
        
    @pseudonym.setter
    def pseudonym(self, new_pseudonym):
        self.__pseudonym = new_pseudonym
        
    @property
    def writer(self):
        return self.__writer
    
    @property    
    def genre(self):
        return self.__genre  
    
    @genre.setter
    def genre(self, new_genre):
        self.__genre = new_genre
        
    @property
    def age_restricted(self):
        return self.__age_restricted
    
    @age_restricted.setter
    def age_restricted(self,age_restricted):
        self.__age_restricted = age_restricted
        
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, new_status):
        self.__status = new_status
        
    @property
    def prologue(self):
        return self.__prologue
    
    @prologue.setter
    def prologue(self, new_prologue):
        self.__prologue = new_prologue
        
    @property
    def date_time(self):
        return self.__date_time
    
    #ตรงนี้แปลกๆ ไม่ควรเป็น property งี้
    @date_time.setter
    def date_time(self, now):
        self.__date_time = datetime.now()
        
    @property
    def date_time_str(self):
        return self.__date_time.strftime("%d/%m/%Y, %H:%M:%S")

    @property
    def chapter_list(self):
        return self.__chapter_list
    
    def add_chapter_list(self,chapter):
        if isinstance(chapter,Chapter):
            self.__chapter_list.append(chapter)

    @property
    def report_list(self):
        return self.__report_list

    @property
    def comment_list(self):
        return self.__comment_list
    
    @property
    def chapter_count(self):
        return len(self.__chapter_list)
    
    def add_comment_list(self, comment):
        if isinstance(comment, Comment):
            self.__comment_list.append(comment)
            
    ###
    def add_report_list(self, report):
        if isinstance(report, Report):
            self.__report_list.append(report)
            
    def add_report_list(self, report):
        self.report_list.append(report)
        self.counting_date_time = datetime.now()
    
    #if add to list = -> +=
    def add_tag(self, tag_list):
        self.__tag += tag_list
        
    #อันนี้งงมาก
    def delete_tag(self, tag_list):
        new_tag_list = []
        for tag in self.__tag:
            if tag not in tag_list: #เพิ่มแท็กที่ไม่อยู่ใน tag_list จาก tagเดิม
                new_tag_list.append(tag)
        self.__tag = new_tag_list
        
    def delete_tag_jin(self, tag_list):
        for tag in tag_list:
            if tag in self.__tag:
                self.__tag.remove(tag)

    def counting_report(self,report_type_list):
        # count_report_list =[]
        for report_type in report_type_list:
            report_count = 0
            for report in self.__report_list:
                if report_count == 10:
                    self.status = "hiding"
                elif report.report_type == report_type:
                    report_count += 1
                    print("report_count",report_count)


    def delete_report(self, report):
        if report in self.report_list:
            self.report_list.remove(report)
    
    def is_chapter_valid(self,chapter_number):
        for chapter in self.chapter_list:
            if chapter.chapter_number == chapter_number:
                return False
        return True
    
    def show_age_restricted(self):
        if self.__age_restricted:
            return "/"
        return "X"
    
    def show_book_info(self,writer,report_type_list):
        self.counting_report(report_type_list)
        if self.status.lower() == "publishing" or writer == self.__writer:
            return {"name" : self.__name,
                    "pseudonym" : self.__pseudonym,
                    "genre" : self.__genre,
                    "status" : self.__status,
                    "prologue" : self.prologue,
                    "age_retricted" : self.show_age_restricted(),
                    "chapter_count" : self.chapter_count,
                    "comments" : self.show_comment_list(),
                    "writer_name": self.__writer.username,
                    "date_time": self.date_time_str,
                    "message" : "This book is publishing or You are a writer" }
        else:
            return {"message": "This book is not publishing"}
        
    def show_comment_list(self):
        comment_list = []
        for comment in self.__comment_list:
            comment_list.append(comment.show_comment())
        return comment_list

    def show_chapter_list(self):
        chapter_list = []
        for chapter in self.__chapter_list:
            chapter_list.append(chapter.show_chapter_briefly())
        return chapter_list
    
    def show_report_list(self):
        report_list = []
        for report in self.__report_list:
            report_list.append(report.show_report())
        return report_list
    
    