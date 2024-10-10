import pandas as pd
import matplotlib.pyplot as plt

courselist = ["CCIT","CCDM","CCNS"]
courseID = [101,102,103]

#to use panda's Dataframe function
#create a dictionary
courseDict = {'course':courselist,'ID':courseID}

#use function --> DATAFRAME
myvariable = pd.DataFrame(courseDict)
#print(myvariable)

# Panda Series
myvariable2 = pd.Series(courseDict)
print(myvariable2) 

#reading csv files
pulsedata = pd.read_csv('Pulse.csv')
#print (myvariable3)

update1 = pulsedata.dropna() #removes empty cells
#print(update1)

#changing data format
update2 = pd.read_csv('Pulse.csv')
update2 ['Date'] = pd. to_datetime (update2["Date"])
#YYY-MM-DD
#print(update2)

#change value
pulsedata.loc[10,'Pulse']=111
#print(pulsedata)
#Using MathPlot and pandas
pulsedata = pd.read_csv('Pulse.csv')
pulsedata.plot(kind='scatter',x='Duration', y='Calories')
