class Bank:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self,amaout):
        if self.is_valid_amaout(amaout):
            self.__balance += amaout
        else:
            print("mablag manfiy bolmaydi")

    def withdraw(self,amaout):
        if not self.is_valid_amaout(amaout):
            print("mablag manfiy bolishi mumkin emas")
        elif amaout > self.__balance:
            print("mablag yetarli emas")
        else:
            self.__balance -= amaout

    def get_balance(self):
        return self.__balance
    
    # shu metodni statik metod qiling, chunki self ga bog'liq emas
    def is_valid_amaout(self,amaout):        
        return isinstance(amaout,(int,float)) and amaout > 0  
    
    def transfer_to(self,boshqa_acc,amaout):
        if not isinstance(boshqa_acc,Bank):
            print("notogri xisob")
            return
        if not self.is_valid_amaout(amaout):
            print("xatolik pul miqdori notogri")
            return
        if amaout > self.__balance:
            print("Summa yetarli emas")
            return
        
        self.__balance -= amaout
        boshqa_acc.__balance += amaout # buni metod orqali ishlatgan yaxshi        
        print(f"{amaout} sum {boshqa_acc.owner} ga mablag tushdi")

account1 = Bank("Ali", 500)
account2 = Bank("Vali", 300)

account1.deposit(200)          
account1.withdraw(100)         
print(account1.get_balance())  

account1.deposit(-50)         
account1.withdraw(1000)       

account1.transfer_to(account2, 200)   
print(account1.get_balance())        
print(account2.get_balance())     