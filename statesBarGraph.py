print("derave1577")

# import the libraries
import matplotlib.pyplot as plt
import csv

# create arrays for the axises of the bar graph
x = [] 
y = []

# saves the file path of the csv file into a variable for ease of use
path="C:\\PythonFiles\\states.csv"

# opens the file in read mode and gives the method the alias csvfile
with open(path, 'r') as csvfile:
    # creates a list from the contents of the csv file
    plots = csv.reader(csvfile, delimiter = ',')
    # fills the empty axis arrays with the data values of the csv file
    for row in plots:
        x.append(row[0])
        y.append(int(row[1]))

# Sets titles and graphical values for the bar graph
plt.bar(x,y,color="g",width=0.72,label="States Visted")
plt.xlabel("States")
plt.ylabel("Times Visited")
plt.title("5 States I Have Visited")
# outputs a bar graph for the csv file
plt.show()
