#Importing the packages required
import pandas as pd 
import time
import csv

#read the csv file
df = pd.read_csv(r"D:\\ERC20 transaction dataset\\ERC20Transactions11.csv")

#creating a function which converts the format of the timeStamp
def time_format(timeStamp):    #timeStamp = 1671961235
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
    return otherStyleTime      #otherStyleTime = 2013--10--10 23:40:00

#picking the timeStamp column and applying the function to each row of the column.
#creating a new column altogether
df['diffTimeStamp']=df['timestamp'].apply(time_format)

#Changing the index's of the column's of the dataset
df = df.reindex(columns=['blockNumber', 'timestamp','diffTimeStamp', 'transactionHash', 'tokenAddress', 'from', 'to', 'fromIsContract', 'toIsContract', 'value'])

#updating and saving the csv file. 
df.to_csv(r"D:\\ERC20 transaction dataset\\ERC20Transactions11.csv", index=False)