import csv

MONTH = 'may'

file = f"{MONTH}.csv"

transactions = []

running_balance = [0]

with open(file, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        date = row[0]
        name = row[1]
        category = 'other'
        amount = float(row[2])
        balance = float(row[3])
        transaction = ((date, name, category, amount))
        print(transaction)