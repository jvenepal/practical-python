# follow.py
import os
import time

# 'producer -> processing -> processing -> consumer' pipeline

# producer
def follow(filename):
    '''Follow the tail of a file.'''
    f = open(filename)
    f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)   # Sleep briefly and retry
            continue
        yield line

# processing
def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line

# consumer
def main():
    import report
    portfolio = report.read_portfolio('Data/portfolio.csv')

    for line in follow('Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')

if __name__ == '__main__':
    main()
