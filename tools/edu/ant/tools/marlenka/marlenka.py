import os
import csv

# not working, currently discontinued

file_name = "test2.csv"
file_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(file_dir)
file_location = parent_dir + "/resources/top_secret/"

with open(file_location + file_name, encoding='iso8859_3') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 18:
            print(f'Column names are: {"| ".join(row)}')
            line_count += 1
        if line_count > 18:
            print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
            line_count += 1
        line_count += 1
print(f'Processed {line_count} lines.')