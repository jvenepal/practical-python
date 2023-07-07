# pcost.py
#
# Exercise 1.27, 1.30
def portfolio_cost(filename):
    'Returns the total portfolio cost.'
    total_cost = 0
    with open(filename, 'rt') as fp:
        #header = next(fp) # skip 1st line
        for linenum, line in enumerate(fp, start=0):
            try :
                _, num_shares, share_price = line.strip().split(',')
                total_cost += float(num_shares) * float(share_price)
            except ValueError:
                print('Row ', linenum, 'Couldn\'t parse line:', line, end='')
    return total_cost

# exer 2.16
import csv
def portfolio_cost(filename):
    tot_cost = 0
    with open(filename, 'rt') as fp:
        data = csv.reader(fp)
        header = next(data)
        for linenum, row in enumerate(data, start=1):
            record = dict(zip(header, row))
            try:
                num_shares = int(record['shares'])
                share_price = float(record['price'])
                tot_cost += num_shares * share_price
            except ValueError:
                print(f'Row {linenum}: Can\'t process: {record}')
            except KeyError:
                print(f'Row {linenum}: key error in line: {record}')

    return tot_cost

def portfolio_cost_csv(filename):
    'Returns the total portfolio cost.'
    import csv
    total_cost = 0
    fp = open(filename, 'rt')
    for line in csv.reader(fp):
        try :
            num_shares, share_price = line[1:]
            total_cost += float(num_shares) * float(share_price)
        except ValueError:
            print('Couldn\'t parse line:', line)
    fp.close()
    return total_cost

# exer 1.33
import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print('Total cost:', cost)
cost = portfolio_cost_csv(filename)
print('Total cost:', cost)
