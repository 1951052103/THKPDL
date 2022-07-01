import csv


def write_title(file):
    with open(str(file), 'w', newline='') as file_out:
        writer = csv.writer(file_out)
        new_row = ['STT'] + ['Code'] + ['Diali'] + ['GDCD'] + ['Hoahoc'] + ['KHTN'] + ['KHXH'] + ['LichSu'] \
                  + ['Ngoaingu'] + ['Nguvan'] + ['Sinhhoc'] + ['Toan'] + ['Vatli'] + ['City']
        writer.writerow(new_row)


def DSHCM():
    with open('Full_Mark_2020.csv', 'r') as file_in:
        reader = csv.reader(file_in, delimiter=',')
        next(reader, None)

        with open(str('DSHCM.csv'), 'a', newline='') as file_out:
            writer = csv.writer(file_out)
            for row in reader:
                if row[13].isdigit():
                    if int(row[13]) == 2:
                        writer.writerow(row)


def DSHN():
    with open('Full_Mark_2020.csv', 'r') as file_in:
        reader = csv.reader(file_in, delimiter=',')
        next(reader, None)

        with open(str('DSHN.csv'), 'a', newline='') as file_out:
            writer = csv.writer(file_out)
            for row in reader:
                if row[13].isdigit():
                    if int(row[13]) == 1:
                        writer.writerow(row)



write_title('DSHCM.csv')
write_title('DSHN.csv')
DSHCM()
DSHN()