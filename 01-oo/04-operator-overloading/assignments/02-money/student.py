class Money:
    def __init__(self,amount,currency):
        self._amount = 0
        self._currency = ""
    def __add__(self,other):
        if self._currency == other.currency:
            return Money(self.amount + other.amount,self._currency)
        else:
            raise ValueError ("Must be the same currency")
    def __sub__(self,other):
        if self._currency == other.currency:
            return Money(self.amount - other.amount,self._currency)
        else:
            raise ValueError ("Must be the same currency")
    def __mul__(self,other):
        if self._currency == other.currency:
            return Money(self.amount - other.amount,self._currency)
        else:
            raise ValueError ("Must be the same currency")