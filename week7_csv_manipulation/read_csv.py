import os
import csv

# csv_file = "/Users/narender/Projects/python/my-python-projects/week7_csv_manipulation/customers-100.csv"
location = os.path.join(os.getcwd(), "week7_csv_manipulation/customers-100.csv")

with open(location, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row)
