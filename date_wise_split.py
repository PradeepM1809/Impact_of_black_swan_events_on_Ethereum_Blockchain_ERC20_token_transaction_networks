#Importing the required packages
import os
import pandas as pd
from os.path import exists

#Base directory path
base = "C:/Users/dyapa/Desktop/MAJORPRO/last/"

#Output directory path
output = "C:/Users/dyapa/Desktop/MAJORPRO/lastout/"

directory = base

#Iterate over all files in directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    print(f)
    
    #Read csv file from dataframe
    df = pd.read_csv(f)
    
    #Get unique timestamps from date columns
    dates = df.diffTimeStamp.unique()
    
    #Iterate over all dates
    for d in dates:
        fname = str(d) + ".csv"
        
        #Slice the data of particular date
        df2 = df.loc[df['diffTimeStamp'] == d]
        new_directory = output
        f_path = os.path.join(new_directory, fname)
        file_exists = exists(f_path)
        
        #Save to file if not exists
        if file_exists:
            df2.to_csv(f_path, mode='a', index=False, header=False)
        
        #Or append to already existing file
        else:
            df2.to_csv(f_path, index=False)
        print("written to file: ", f_path)