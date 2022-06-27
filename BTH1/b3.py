import csv
from math import floor


def get_most_frequent(list):
    counter = 0
    num = list[0]

    for i in list:
        curr_frequency = list.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i

    return num


def check_valid_date(day, month, year):
    days_count = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 400 == 0:
        days_count[2] = 29
    elif year % 4 == 0 and year % 100 != 0:
        days_count[2] = 29

    if 1 <= month <= 12:
        if 1 <= day <= days_count[month-1]:
            return 1
    return 0


def get_valid_day(day, month, year):
    days_count = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 400 == 0:
        days_count[2] = 29
    elif year % 4 == 0 and year % 100 != 0:
        days_count[2] = 29

    if day < 1:
        return 1
    elif day > days_count[month-1]:
        return days_count[month-1]


def read_date_1(data, days, months, years):
    for row in data:
        if row[4] == '' or int(row[4]) < 1:
            continue
        if row[5] == '' or int(row[5]) < 1:
            continue
        if row[6] == '' or int(row[6]) < 1:
            continue

        years.append(row[6])
        if int(row[5]) > 12:
            days.append(row[5])
            months.append(row[4])
        else:
            days.append(row[4])
            months.append(row[5])


def read_date_2(data, days, months, years):
    for row in data:
        date = str(row[4]).split('-')
        if len(date) == 1:
            years.append(date[0])
        else:
            years.append(date[0])
            days.append(date[2])
            months.append(date[1])


def read_date_3(data, days, months, years):
    for row in data:
        date = str(row[4]).split('/')

        years.append(date[2])
        days.append(date[0])
        months.append(date[1])


def read_date_4(data, days, months, years):
    for row in data:
        date = str(row[4]).split('-')
        if len(date) == 1:
            if 1970 < int(date[0]) < 10000:
                years.append(date[0])
            else:
                years.append(floor(int(date[0])/10) + int(date[0]) % 10)
        else:
            years.append(date[2])
            days.append(date[0])
            months.append(date[1])


def read_name(data, first_name, last_names):
    for row in data:
        ln = str(row[2]).split(' ')
        first_name.append(str(row[3]))
        last_names.append(ln[0])


def write_title():
    with open('CSV/DSSVFixed.csv', 'w', newline='') as file_out:
        writer = csv.writer(file_out)
        new_row = ['STT'] + ['MSSV'] + ['Ho'] + ['Ten'] + ['Ngay sinh']
        writer.writerow(new_row)


def read_file_1():
    with open('CSV/DSSV1.csv', 'r') as file_in:
        reader = csv.reader(file_in, delimiter=',')
        next(reader, None)

        days = []
        months = []
        years = []
        first_names = []
        last_names = []

        data = list(reader)
        read_date_1(data, days, months, years)
        read_name(filter(any, data), first_names, last_names)

        with open('CSV/DSSVFixed.csv', 'a', newline='') as file_out:
            writer = csv.writer(file_out)

            for row in data:
                day = row[4]
                month = row[5]
                year = row[6]

                if month == '':
                    month = get_most_frequent(months)
                if day == '':
                    day = get_most_frequent(days)
                if year == '':
                    year = get_most_frequent(years)

                if int(month) < 1:
                    month = 1
                if int(day) < 1:
                    day = 1

                if int(month) > 12:
                    day = row[5]
                    month = row[4]
                if int(month) > 12:
                    day = row[4]
                    month = 12

                if not check_valid_date(int(day), int(month), int(year)):
                    day = get_valid_day(int(day), int(month), int(year))

                ln = [str(row[2]).title()]  # last name
                fn = [str(row[3]).title()]  # frist name

                if str(row[2]) == '':
                    ln = [get_most_frequent(last_names)]
                if str(row[3]) == '':
                    fn = [get_most_frequent(first_names)]

                dt = [str(month) + '/' + str(day) + '/' + str(year)] # month/day/year
                new_row = row[0:1+1] + ln + fn + dt
                writer.writerow(new_row)


def read_file_2():
    with open('CSV/DSSV2.csv', 'r') as file_in:
        reader = csv.reader(file_in, delimiter=',')
        next(reader, None)

        days = []
        months = []
        years = []

        first_names = []
        last_names = []

        data = list(reader)
        read_date_2(filter(any, data), days, months, years)
        read_name(filter(any, data), first_names, last_names)

        with open('CSV/DSSVFixed.csv', 'a', newline='') as file_out:
            writer = csv.writer(file_out)
            for row in filter(any, data):
                date = str(row[4]).split('-')

                year = date[0]
                if len(date) == 1:
                    day = get_most_frequent(days)
                    month = get_most_frequent(months)
                else:
                    day = date[2]
                    month = date[1]

                if int(month) < 1:
                    month = 1

                if int(month) > 12:
                    month = 12

                if not check_valid_date(int(day), int(month), int(year)):
                    day = get_valid_day(int(day), int(month), int(year))

                dt = [str(month) + '/' + str(day) + '/' + str(year)] # month/day/year

                ln = [str(row[2]).title()] # last name
                fn = [str(row[3]).title()]  # frist name

                if str(row[2]) == '':
                    ln = [get_most_frequent(last_names)]
                if str(row[3]) == '':
                    fn = [get_most_frequent(first_names)]

                new_row = row[0:1+1] + ln + fn + dt
                writer.writerow(new_row)


def read_file_3():
    with open('CSV/DSSV3.csv', 'r') as file_in:
        reader = csv.reader(file_in, delimiter=',')
        next(reader, None)

        days = []
        months = []
        years = []

        first_names = []
        last_names = []

        data = list(reader)
        read_date_3(filter(any, data), days, months, years)
        read_name(filter(any, data), first_names, last_names)

        with open('CSV/DSSVFixed.csv', 'a', newline='') as file_out:
            writer = csv.writer(file_out)
            for row in filter(any, data):
                date = str(row[4]).split('/')

                year = date[2]
                day = date[0]
                month = date[1]

                if int(month) < 1:
                    month = 1

                if int(month) > 12:
                    month = 12

                if not check_valid_date(int(day), int(month), int(year)):
                    day = get_valid_day(int(day), int(month), int(year))

                dt = [str(month) + '/' + str(day) + '/' + str(year)] # month/day/year

                ln = [str(row[2]).title()] # last name
                fn = [str(row[3]).title()]  # frist name

                if str(row[2]) == '':
                    ln = [get_most_frequent(last_names)]
                if str(row[3]) == '':
                    fn = [get_most_frequent(first_names)]

                new_row = row[0:1+1] + ln + fn + dt
                writer.writerow(new_row)


def read_file_4():
    with open('CSV/DSSV4.csv', 'r') as file_in:
        reader = csv.reader(file_in, delimiter=',')
        next(reader, None)

        days = []
        months = []
        years = []

        first_names = []
        last_names = []

        data = list(reader)
        read_date_4(filter(any, data), days, months, years)
        read_name(filter(any, data), first_names, last_names)

        with open('CSV/DSSVFixed.csv', 'a', newline='') as file_out:
            writer = csv.writer(file_out)
            for row in filter(any, data):
                date = str(row[4]).split('-')

                if len(date) == 1:
                    day = get_most_frequent(days)
                    month = get_most_frequent(months)
                    if 1970 < int(date[0]) < 10000:
                        year = date[0]
                    else:
                        year = floor(int(date[0]) / 10) + int(date[0]) % 10
                else:
                    day = date[0]
                    month = date[1]
                    year = date[2]

                if int(month) < 1:
                    month = 1

                if int(month) > 12:
                    month = 12

                if not check_valid_date(int(day), int(month), int(year)):
                    day = get_valid_day(int(day), int(month), int(year))

                dt = [str(month) + '/' + str(day) + '/' + str(year)] # month/day/year

                ln = [str(row[2]).title()] # last name
                fn = [str(row[3]).title()]  # frist name

                if str(row[2]) == '':
                    ln = [get_most_frequent(last_names)]
                if str(row[3]) == '':
                    fn = [get_most_frequent(first_names)]

                new_row = row[0:1+1] + ln + fn + dt
                writer.writerow(new_row)


write_title()
read_file_1()
read_file_2()
read_file_3()
read_file_4()