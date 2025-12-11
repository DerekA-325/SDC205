import matplotlib.pyplot as plt
import csv

path="C:\\PythonFiles\\scores.csv"
fopen = open(path, "w")
fopen.write("John, 75\n")
fopen.write("Mary, 75\n")
fopen.write("Richard, 100\n")
fopen.write("Jane, 90\n")
fopen.flush()
fopen.close

x=[]
y=[]

with open(path, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        x.append(row[0])
        y.append(int(row[1]))
plt.bar(x,y,color="g",width=0.72,label="Scores")
plt.xlabel("Names")
plt.ylabel("Scores")

plt.title("derave1577 Graph Practice")
plt.legend()
plt.show()
