# report.py

import csv
from Work.fileparse import parse_csv
from Work.stock import Stock
import Work.tableformat as tableformat

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    with open(filename, 'rt') as file:
        portdict =  parse_csv(file, select=['name', 'shares', 'price'], types=[str, int, float])
    portfolio = [Stock(d['name'], d['shares'], d['price']) for d in portdict]
    return portfolio


def read_prices(filename):
    with open(filename, 'rt') as file:
        prices =  dict(parse_csv(file, types=[str, float], has_headers=False))
    return prices



def make_report(portfolio, prices):
    reports = []
    for p in portfolio:
        report = (p.name, p.shares, prices[p.name], prices[p.name] - p.price)
        reports.append(report)
    return reports


def print_report(report, formatter):
    headers = ('Name', 'Shares', 'Price', 'Change')
    formatter.headings(headers)
    for name, shares, price, change in report:
        row_data = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(row_data)


def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(argv):
    if len(argv) != 4:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfile pricefile')
    portfolio_file = argv[1]
    prices_file = argv[2]
    formatter = argv[3]
    portfolio_report(portfolio_file, prices_file, formatter)

if __name__ == '__main__':
    import sys
    main(sys.argv)