# fileparse.py
#
# Exercise 3.3
import csv
import logging
log = logging.getLogger(__name__)

# exer 3.3 to 3.7
def parse_csv(lines, has_headers, select=[], types=[], delimiter=None, silence_err=False):
    '''
    Parse a csv file and return a list of records with type conversion
    '''
    if select and has_headers==False and not silence_err:
        raise RuntimeError('select arg requires column header be valid.')

    records = []
    if delimiter:
        rows = csv.reader(lines, delimiter=delimiter)
    else:
        rows = csv.reader(lines)
    startlinenum = 0
    if has_headers:
        header = next(rows)
        startlinenum = 1
    if select:
        idx = [header.index(col) for col in select]
        header = select
    for linen, row in enumerate(rows, start=startlinenum):
        if not row:
            continue
        if select and idx:
            #record = {header[i]: row[i] for i in idx}
            row = [row[i] for i in idx]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_err:
                    #print(f'Row {linen}: Couldn\'t convert row: {row}')
                    #print(f'Row {linen}: {e}')
                    log.warning(f'Row {linen}: Couldn\'t convert row: {row}')
                    log.debug(f'Row {linen}: {e}')

        if has_headers:
            record = dict(zip(header, row))
        else:
            record = tuple(row)
        records.append(record)
    return records
