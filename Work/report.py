# report.py
#
import csv
import sys
from pprint import pprint
from fileparse import parse_csv
import stock
from portfolio import Portfolio

# Exercise 2.4 & exer 2.16
def read_portfolio(filename):
    with open(filename) as lines:
        portdict = parse_csv(lines, has_headers=True, select=['name', 'shares', 'price'],
                     types=[str, int, float], silence_err=False)
        #portfolio = [stock.Stock(pd['name'], pd['shares'], pd['price']) for pd in portdict]
        portfolio = [stock.Stock(**pd) for pd in portdict]
        return Portfolio(portfolio)

# exer 2.6
def read_prices(filename):
    with open(filename) as lines:
        return parse_csv(lines, has_headers=False, types=[str, float])

# exer 2.7
##gain = 0
##for entry in portfolio:
##    gain += entry['shares'] * (prices[entry['name']] - entry['price'])
##print('gain is:', gain)

# exer 2.9
def make_report(portfolio, prices):
    table = []
    for entry in portfolio:
        #name, shares, price = (entry['name'], entry['shares'], entry['price'])
        name, shares, price = entry.name, entry.shares, entry.price
        change = prices[name] - price
        table.append((name, shares, prices[name], change))
    return table

#report = make_report(portfolio, prices)
# exer 2.10 & exer 3.1
def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    separator = tuple(['-' * 10] * 4)
    for row in (headers, separator):
        print('%10s %10s %10s %10s' % row)
    for row in report:
        print('%10s %10d %10.2f %10.2f' %row)

import tableformat
def print_report(report, formatter):
    formatter.headings(['name', 'shares', 'price', 'change'])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

# exer 3.2
def portfolio_report(portfolio_file, prices_file, fmt='txt'):
    portfolio = read_portfolio(portfolio_file)
    prices = dict(read_prices(prices_file))
    #print_report(make_report(portfolio, prices))
    report = make_report(portfolio, prices)

    formatter = tableformat.createformatter(fmt)
    print_report(report, formatter)

def main(argv):
    if len(argv) == 3:
        portfolio_file = argv[1]
        prices_file = argv[2]
        fmt = 'txt'
    elif len(argv) == 4:
        portfolio_file = argv[1]
        prices_file = argv[2]
        fmt = argv[3]
    else:
        portfolio_file = './Data/portfolio.csv'
        prices_file = './Data/prices.csv'
        fmt = 'txt'
    portfolio_report(portfolio_file, prices_file, fmt)

if __name__ == '__main__':
    import sys
    main(sys.argv)
