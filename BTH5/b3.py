import csv


def write_title(file):
    with open(str(file), 'w', newline='') as file_out:
        writer = csv.writer(file_out)
        new_row = ['Age'] + ['Gender'] + ['MaritalStatus'] + ['EducationLevel'] + ['EducationBackground'] + ['JobRole']\
                  + ['EnvironmentSatisfaction'] + ['RelationshipSatisfaction'] + ['WorkLifeBalance']\
                  + ['TotalWorkExperienceInYears'] + ['ExperienceYearsInCurrentRole'] + ['PerformanceResult']
        writer.writerow(new_row)


def add_train_data():
    with open('Collected_Hr_data_performances.csv', 'r', encoding="utf8") as file_in:
        reader = csv.reader(file_in, delimiter=",")
        next(reader, None)
        count = 0

        with open(str('train_data.csv'), 'a', newline='') as file_out:
            writer = csv.writer(file_out)
            for row in reader:
                count += 1
                if count <= 1000:
                    new_row = row[2:4+1] + row[6:8+1] + row[10:11] + row[12:13] + row[14:15] + row[16:17] \
                              + row[18:19] + row[20:21]
                    writer.writerow(new_row)


def add_test_data():
    with open('Collected_Hr_data_performances.csv', 'r', encoding="utf8") as file_in:
        reader = csv.reader(file_in, delimiter=",")
        next(reader, None)
        count = 0

        with open(str('test_data.csv'), 'a', newline='') as file_out:
            writer = csv.writer(file_out)
            for row in reader:
                count += 1
                if count > 1000:

                    new_row = row[2:4+1] + row[6:8+1] + row[10:11] + row[12:13] + row[14:15] + row[16:17] \
                              + row[18:19] + row[20:21]
                    writer.writerow(new_row)


write_title('train_data.csv')
write_title('test_data.csv')
add_train_data()
add_test_data()