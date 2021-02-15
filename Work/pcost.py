# pcost.py
# Exercise 1.27
import csv
import sys


def portfolio_cost(file):
    total_cost = 0
    with open(file, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for index, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                shares = int(record['shares'])
                price = float(record['price'])
                total_cost += shares * price
            except ValueError:
                print(f'Row{index}: Could not convert {row}')
    return total_cost


if len(sys.argv) == 2:
    print(sys.argv)
    filename = sys.argv[1]
else:
    filename = 'Work/Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'total cost {cost}')
