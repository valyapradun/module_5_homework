from collections import defaultdict
import csv


def get_top_performers(file_path, number_of_top_students=5):
    """
    File data/students.csv stores information about students in CSV format.
    This file contains the student’s names, age and average mark.
    Implement a function which receives file path and returns names of top performer students.
    """
    temp_dict = defaultdict(float)

    with open(file_path, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            temp_dict[row[0]] = float(row[2])

    res = sorted(temp_dict, key=temp_dict.get, reverse=True)
    return res[0:number_of_top_students]


def sort_ages(original_file, sorted_file):
    """
    Implement a function which receives the file path with students info and writes CSV student information
    to the new file in descending order of age.
    """

    with open(original_file, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = next(csv_reader)
        all_students = list(csv_reader)

    all_students.sort(key=lambda student: int(student[1]), reverse=True)

    with open(sorted_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(header)
        csv_writer.writerows(all_students)


if __name__ == '__main__':
    print(get_top_performers(file_path='./data/students.csv', number_of_top_students=5))
    sort_ages(original_file='./data/students.csv', sorted_file='./data/sorted_ages.csv')
