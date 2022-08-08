import csv


def write_title(file):
    with open(str(file), 'w', newline='') as file_out:
        writer = csv.writer(file_out)
        new_row = ['age'] + ['sex'] + ['region'] + ['income'] + ['married'] + ['children']\
                  + ['car'] + ['save_act'] + ['current_act'] + ['mortgage'] + ['pep']
        writer.writerow(new_row)


def add_train_data(read_file, write_file, limit):
    with open(str(read_file), 'r', encoding="utf8") as file_in:
        reader = csv.reader(file_in, delimiter=",")
        next(reader, None)
        count = 0

        with open(str(write_file), 'a', newline='') as file_out:
            writer = csv.writer(file_out)
            for row in reader:
                count += 1
                if count <= int(limit):
                    new_row = row[1:11+1]
                    writer.writerow(new_row)


def add_test_data(read_file, write_file, limit):
    with open(str(read_file), 'r', encoding="utf8") as file_in:
        reader = csv.reader(file_in, delimiter=",")
        next(reader, None)
        count = 0

        with open(str(write_file), 'a', newline='') as file_out:
            writer = csv.writer(file_out)
            for row in reader:
                count += 1
                if count > int(limit):
                    new_row = row[1:11 + 1]
                    writer.writerow(new_row)


write_title('train_data.csv')
write_title('test_data.csv')
add_train_data('bank-data.csv', 'train_data.csv', 480)
add_test_data('bank-data.csv', 'test_data.csv', 480)