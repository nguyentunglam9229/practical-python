# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(file, select=None, types=None, has_headers=True, delimiter=',', silence_error=False):
    """
    parse a csv file into a list of record
    """
    # cannot have select and has_headers=False at the same time
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    rows = csv.reader(file, delimiter=delimiter)

    # read the filename headers if any
    headers = next(rows) if has_headers else []

    if select:
        indices = [headers.index(column) for column in select]
        headers = select
    else:
        indices = []
    records = []
    for i, row in enumerate(rows, start=1):
        if not row:     # skip for row with no data
            continue

        # pick up indices in select
        try:
            if indices:
                row = [row[column] for column in indices]

            # apply type conversion
            if types:
                row = [func(val) for func, val in zip(types, row)]

            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
        except ValueError as e:
            if not silence_error:
                print(f'Row {i}: Could not convert {row}')
                print(f'Row {i}: Reason {e}')
    return records
