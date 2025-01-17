# ticker.py

from follow import follow
import csv
import report
import tableformat

def select_columns(rows, indices):
    for row in rows:
        yield [row[idx] for idx in indices]
        #return [row[idx] for idx in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

if __name__ == '__main__':
    lines = follow('Data/stocklog.csv')
    portfolio = report.read_portfolio('Data/portfolio.csv')
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)
    for row in rows:
        print(row)

def ticker(portfile, logfile, fmt):
    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    rows = filter_symbols(rows, portfolio)

    formatter = tableformat.createformatter(fmt)
    headers = ['name', 'price', 'change']
    formatter.headings(headers)
    for row in rows:
        formatter.row(row.values())
