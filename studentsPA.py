print("derave1577")
import pandas as pd
import matplotlib.pyplot as plt

# create the array of students
students = [['John', 'John', 'Jack', 'Jack', 'Jim', 'Jim', 'Susie', 'Susie', 'Sarah', 'Sarah', 'Sam', 'Sam', 'Paul', 'Paul', 'Tom', 'Tom', 'Kate', 'Kate', 'Mary', 'Mary'], ['Math', 'English', 'Math', 'English', 'Math', 'English', 'Math', 'English', 'Math', 'English', 'Math', 'English', 'Math', 'English', 'Math', 'English', 'Math', 'English', 'Math', 'English']]
# create the index of students and subjects
index = pd.MultiIndex.from_arrays(students, names = ('Student', 'Subject'))
# creates a data frame for the grades for each student in each subject based on the index
df = pd.DataFrame({'Grades': [90, 87, 88, 92, 78, 84, 96, 85, 87, 93, 73, 77, 92, 94, 83, 82, 89, 91, 71, 76]}, index = index)

# group by the mean of the subject
averageGrade = df.groupby(by = ["Subject"]).mean()

# display the data frame
print(averageGrade)

# display a vertical bar graph
averageGrade['Grades'].plot(kind = 'bar')

plt.xlabel("Average Grade by Subject")
plt.xticks(rotation = 0)
plt.title("derave1577 Average Grades")
plt.show()
