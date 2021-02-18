# pcost.py
# Exercise 1.27
import csv
import sys
from Work.report import read_portfolio


def portfolio_cost(file):
    total_cost = 0
    records = read_portfolio(file)
    total_cost = sum([record.cost() for record in records])
    return total_cost


def main(argv):
    if len(sys.argv) == 2:
        print(sys.argv)
        filename = sys.argv[1]
    else:
        filename = 'Work/Data/portfolio.csv'

    cost = portfolio_cost(filename)
    print(f'total cost {cost}')

if __name__ == '__main__':
    import sys
    main(sys.argv)