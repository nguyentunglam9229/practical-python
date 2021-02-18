class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        thead = ''
        for header in headers:
            thead += f'<th>{header}</th>'
        print(f'<tr>{thead}</tr>')

    def row(self, rowdata):
        td = ''
        for data in rowdata:
            td += f'<td>{data}</td>'
        print(f'<tr>{td}</tr>')

class FormatError(Exception):
    pass

def create_formatter(fmt):
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'unknow formatter {fmt}')


def print_table(objs, attrs, formatter):
    formatter.headings(attrs)
    for obj in objs:
        formatter.row([str(getattr(obj, attr)) for attr in attrs])