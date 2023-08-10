import csv

MONTH = 'may'

file = f"{MONTH}.csv"

transactions = []

running_balance = [0]

Subscriptions = {'Spotify USA', 'MYBESTBUY', 'MICROSOFT YEARLY'}

with open(file, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        date = row[0]
        name = row[1]
        category = 'other'
        if name == "Trader Joes Comp":
            category = 'Paycheck'
        amount = float(row[2])
        balance = float(row[3])
        transaction = ((date, name, category, amount))
        print(transaction)