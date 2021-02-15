# report.py

import csv


def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows):
            holding = dict(zip(headers, row))
            holding['shares'] = int(holding['shares'])
            holding['price'] = float(holding['price'])
            portfolio.append(holding)
    return portfolio


def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        try:
            for row in rows:
                prices[row[0]] = float(row[1])
        except IndexError:
            print('bad value: ', row)
    return prices


def make_report(portfolio, prices):
    reports = []
    for p in portfolio:
        report = (p['name'], p['shares'], prices[p['name']], prices[p['name']] - p['price'])
        reports.append(report)
    return reports


portfolio = read_portfolio('Work/Data/portfolio.csv')
prices = read_prices('Work/Data/prices.csv')
portfolio_value = 0.0
for p in portfolio:
    portfolio_value += p['shares'] * prices[p['name']]

profit = 0.0
for p in portfolio:
    profit += p['shares'] * (prices[p['name']] - p['price'])

print("portfolio_value: ", portfolio_value)
print('profit: ', profit)

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
report = make_report(portfolio, prices)
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
