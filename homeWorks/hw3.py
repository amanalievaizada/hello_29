class Bank:
    def __init__(self,name,balance):
     self._name = name
     self._balance = balance


    def moneyx(self,amount):
     self._balance += amount

    def kill(self):
      self.balance =0

    def _jackpot(self):
      self._balance *=10

    def _total_balance(self,other):
     self.balance+=other._balance


custom1 = Bank('custom1',1000)
custom2 = Bank('custom2',2000)
print('custom1:',custom1._balance)
print('custom2:',custom2._balance)
