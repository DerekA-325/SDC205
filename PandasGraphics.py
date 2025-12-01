print("derave1577")
import matplotlib.pyplot as plt
import pandas as pd

data1 = {'Ballrooms':['Ballroom 1','Ballroom 2','Ballroom 3'],'Capacity':[25000,11000,5000]}
data2 = {'Attendees':[18000,13000,10000]}

df1 = pd.DataFrame(data1, columns=['Ballrooms','Capacity'])
df2 = pd.DataFrame(data2, index=['Children','Adults','Teens'])
print(df1)

df1.plot(x='Ballrooms',y='Capacity', kind='bar')
df2.plot.pie(y='Attendees')
plt.show()
