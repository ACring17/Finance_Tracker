import csv

MONTH = 'may'

file = f"{MONTH}.csv"

with open(file, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)