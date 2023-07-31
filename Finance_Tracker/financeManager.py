import csv

MONTH = 'may'

file = f"{MONTH}.csv"

with open(file, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        date = row[0]
        name = row[1]
        amount = float(row[2])
        print(row)