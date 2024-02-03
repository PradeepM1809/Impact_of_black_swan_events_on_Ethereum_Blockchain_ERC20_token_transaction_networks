#Importing the required packages
import os
import pandas as pd

#Dictionary to give labels for each hash key
tockendict = {}

#ID variable to start labeling with 0
t_id = 0
token = "token"

#Base directory path
base ="C:/Users/dyapa/Desktop/MAJORPRO/test/"

#Output dircetory path
output ="C:/Users/dyapa/Desktop/MAJORPRO/testout/"

directory = base

#Iterate over all files in the directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    print(f)
    
    #Read a csv file to pandas dataframe
    df = pd.read_csv(f)
    
    #Two new columns for from and to label
    df['tokenLabel'] = 0
    
    #Iterate over all the rows in dataframe
    for i in range(len(df['tokenAddress'])):
        
        #If from hash key is in directory use its value from dictionary
        if df['tokenAddress'][i] in tockendict:
            df['tokenLabel'][i] = tockendict[df['tokenAddress'][i]]
            
        #If not assign the next label and store in dataframe and dictionary
        else:
            tockendict[df['tokenAddress'][i]] = token + str(t_id)
            df['tokenLabel'][i] = tockendict[df['tokenAddress'][i]]
            id += 1
    
    #Extract only these columns
    df2 = df[['diffTimeStamp','tokenAddress','tokenLabel','from' , 'to']]
    new_directory = output
    f = os.path.join(new_directory, filename)
    print("updated ", f)
    
    #Save to new csv file
    df2.to_csv(f, index=False)