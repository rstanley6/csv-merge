import csv

#csv_list = list()

with open('my.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row[0])
        print(row[1])
        print(row[2])
        print(row[3])
