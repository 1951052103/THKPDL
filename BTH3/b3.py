import csv

with open('car.csv', 'r', encoding="utf8") as file_in:
    reader = csv.reader(file_in, delimiter="|")
    count = 0

    for row in reader:
        print(row)
        count += 1
        if count > 100:
            break
