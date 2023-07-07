# report.py
#
import csv
import sys
from pprint import pprint

# Exercise 2.4 & exer 2.16
def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as fp:
        rows = csv.reader(fp)
        header = next(rows)
        for linenum, row in enumerate(rows, start=1):
            record = dict(zip(header, row))
            try:
                portfolio.append({
                    'name': record['name'],
                    'shares': int(record['shares']),
                    'price': float(record['price'])})
            except ValueError:
                print(f'Line {linenum}: Can\'t process: line')
    return portfolio

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
portfolio = read_portfolio(filename)

# exer 2.5
def read_portfolio_d(filename):
    portfolio = []
    with open(filename, 'rt') as fp:
        rows = csv.reader(fp)
        header = next(rows)
        for row in rows:
            portfolio.append({'name': row[0],
                             'price': float(row[2]),
                             'shares': int(row[1])})
    return portfolio
#portfolio = read_portfolio_d(filename)

# exer 2.6
def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as fp:
        rows = csv.reader(fp)
        try:
            for smbl, price in rows:
                prices[smbl] = float(price)
        except ValueError:
            pass
    return prices

prices = read_prices('Data/prices.csv')
#pprint(prices)

# exer 2.7
gain = 0
for entry in portfolio:
    gain += entry['shares'] * (prices[entry['name']] - entry['price'])
print('gain is:', gain)

# exer 2.9
def make_report(portfolio, prices):
    table = []
    for entry in portfolio:
        name, shares, price = (entry['name'], entry['shares'], entry['price'])
        change = prices[name] - price
        table.append((name, shares, prices[name], change))
    return table

report = make_report(portfolio, prices)
# exer 2.10
headers = ('Name', 'Shares', 'Price', 'Change')
separator = tuple(['-' * 10] * 4)
for row in (headers, separator):
    print('%10s %10s %10s %10s' % row)
for row in report:
    print('%10s %10d %10.2f %10.2f' %row)
