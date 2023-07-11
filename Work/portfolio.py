
class Portfolio:
    def __init__(self, holdings:list):
        '''
        holdings is a list of stock objects
        '''
        self._holdings = holdings

    @property
    def total_cost(self):
        #return sum([stock.cost for stock in self._holdings])
        return sum(stock.cost for stock in self._holdings) # generator comprehension

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for stock in self._holdings:
            total_shares[stock['name']] += stock.shares
        return total_shares

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, idx):
        return self._holdings[idx]

    def __contains__(self, name):
        return name in [stock.name for stock in self._holdings]
