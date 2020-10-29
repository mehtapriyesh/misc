# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 00:18:33 2020

@author: user
"""

from datetime import datetime

def now():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")

class Bank():
    
    total = 1
    
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.bal = balance
        self.acc = Bank.total
        self.status = []
        Bank.total += 1

    def withdraw(self, amt):
        if self.bal > amt:
            self.bal -= amt            
        else:
            print("Withdrawal prohibited.")
        self.getbal()
        self.status.append("Withdrawn {} at {}. Remaining Balance {}.".format(amt, now(), self.bal))
        
    def deposit(self, amt):
        self.bal += amt
        self.getbal()
        self.status.append("Deposit {} at {}. Remaining Balance {}.".format(amt, now(), self.bal))

    def getbal(self):
        print("Available balance is: ", self.bal)

    def getstatement(self):
        print("Transactions for Account number:", self.acc)
        return self.status



class Current(Bank):
    total = 0
    
    def __init__(self, owner, balance, od):    
        super().__init__(owner, balance)
        Current.total+=1
        self.acc = "C"+f'{Current.total:06}'
        self.od = od    
        
    def update_od(self, new_od):
        self.od = new_od
    
    def withdraw(self, amt):
        if self.bal - amt > self.od:
            self.bal -= amt
            self.status.append("Withdrawn {} at {}. Remaining Balance {}.".format(amt, now(), self.bal))
        else:
            print("Withdrawal prohibited. Crossed Overdraft Limit")
        super().getbal()
        
class Saving(Bank):
    total = 0       
    
    def __init__(self, owner, balance):    
        super().__init__(owner, balance)
        Saving.total+=1
        self.acc = "S"+f'{Saving.total:06}'
    

            
                 
            
obj = Current("Habib",875,250)                
obj.update_od(-225)
obj.getbal()
obj.deposit(125)
obj.withdraw(110)
obj.withdraw(800)        
obj.withdraw(250)
obj.status        
obj.getstatement()


    
obj2 = Saving("Javed", 9200)
obj2.deposit(800)

obj2.acc
obj.acc


