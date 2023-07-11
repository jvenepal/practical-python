from typedproperty import typedproperty
from typedproperty import String, Integer, Float

class Stock:
    #__slots__ = ('name', 'shares', 'price')
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        '''
        Returns the cost of a stock.
        '''
        return self.shares * self.price

    def sell(self, nshares):
        '''
        Sell 'nshares' shares of a stock
        '''
        self.shares -= nshares

    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'
