import os

directory = "lots_of_empty_text_files"

parent_dir = os.path.dirname(os.path.abspath(__file__))

path = os.path.join(parent_dir, directory)

if not os.path.exists(path):
	os.mkdir(path)
	print("Directory '%s' created" %directory)
else:
	print(f"Directory '{directory}' already exists.")
	quit()

n = 1

while n < 101:
	filename  = f"file_{n:03}.txt"
	with open(os.path.join(path, filename), "w") as f:
		pass
	n += 1

print("100 empty .txt files created.")

files = os.listdir(path)

for i in files:
	if i.endswith(".txt") and not i.startswith("backup_"):
		newname = 'backup_' + i
		os.rename(os.path.join(path, i), os.path.join(path, newname))


