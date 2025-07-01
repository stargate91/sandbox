import os

parent_dir = os.path.dirname(os.path.abspath(__file__))

filename = "log.txt"

error_counter = 0

with open(os.path.join(parent_dir, filename), "r") as f:
	for line in f.readlines():
		if 'ERROR' in line:
			error_counter += 1

print(f"The log contains {error_counter} errors.")