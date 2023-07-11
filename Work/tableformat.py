
class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for data in rowdata:
            print(f'{str(data):>10s}', end=' ')
        print()

class CsvTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))
    def row(self, rowdata):
        print(','.join(rowdata))

class FormatError(Exception):
    pass

def createformatter(fmt='txt'):
    if fmt == 'txt':
        formatter = TextTableFormatter()
    elif fmt == 'csv':
        formatter = CsvTableFormatter()
    else:
        raise FormatError(f'Unsopported format {fmt}')
    return formatter

def print_table(objs, attrs, fmtr):
    '''
    Prints user specified attributes 'attrs' of a list of arbitary objects 'obj' 
    in the specified format 'fmtr'
    objs:       list of arbitary objects
    attrs:      list of attributes of obj to print
    fmtr:       desired output format for printing
    '''
    fmtr.headings(attrs)
    for obj in objs:
        rowdata = [getattr(obj, attr) for attr in attrs]
        fmtr.row(rowdata)

