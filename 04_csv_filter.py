import csv
import os

parent_dir = os.path.dirname(os.path.abspath(__file__))

csv_file = "scores.csv"

with open(os.path.join(parent_dir, csv_file), mode ='r') as f:
	_csv_file = csv.reader(f)
	heading = next(_csv_file)
	for index, line in enumerate(_csv_file, start=2):
		x = int(line[1])
		if x > 100:
			print(f"{index}. {line[1]}")