print("derave1577")
import csv
path="C:\\PythonFiles\\states.csv"
with open(path, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
f.close
