import Controller as Controller

class PaymentMethod:
    def __init__(self):
        self.__name = ""
    #=================================
    @property
    def name(self):
        return self.__name
    #=================================method   
    def buy_coin(self, price):
        pass

class OnlineBanking(PaymentMethod):
    def __init__(self, account_id):
        self.__name = 'OnlineBanking'
        self.__account_id = account_id
    #==================================
    @property
    def name(self):
        return self.__name
    @property
    def account_id(self):
        return self.__account_id
    
class DebitCard(PaymentMethod):
    def __init__(self, card_id):
        self.__name = 'Debit Card'
        self.__card_id = card_id
    #==================================
    @property
    def name(self):
        return self.__name
    @property
    def card_id(self):
        return self.__card_id
    

class TrueMoneyWallet(PaymentMethod):
    def __init__(self, phone_number):
        self.__name = 'TrueMoney Wallet'
        self.__phone_number = phone_number
    #==================================
    @property
    def name(self):
        return self.__name
    @property
    def phone_number(self):
        return self.__phone_number