#Importing the required packages
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

#Storing the path details of the directory of the dataset
base = "D:\\ERC20DATASET\\pradeep"

directory = base

#Creating a empty list
CompleteDetails = []

#The complete datasets was divided in terms of date. So picking each day's csv file in a sequence of date.
for filename in sorted(os.listdir(directory)):
  #joining the path and the filename
  f = os.path.join(directory, filename)

  #Reading the csv file
  df = pd.read_csv(f)

  #creating a empty multi directional graph
  G = nx.MultiDiGraph()

  #adding nodes and edges to the graph G
  for row in df.iterrows():
    if row[1].From not in G:
      G.add_node(row[1].From)
    if row[1].to not in G:
      G.add_node(row[1].to)
    G.add_edge(row[1].From,row[1].to)

  #Creating a dictionary of the list of tuples of In_Degree and Out_Degree of nodes in the graph
  # Example : tuple ('0xfc1e1fd1d25d915c7eae1ece7112eb141dca540d',48) into dictionary {'0xfc1e1fd1d25d915c7eae1ece7112eb141dca540d': 48}
  InDegree = dict(G.in_degree())
  OutDegree = dict(G.out_degree())

  #Creating a separate list of the values of In_Degree and Out_Degree of the nodes from the above created dictionary.
  InDegree_value = list(InDegree.values())
  OutDegree_value = list(OutDegree.values())

  #Extracting the maximum value of In_Degree and Out_Degree from each list.
  MaxIn = max(InDegree_value)
  MaxOut = max(OutDegree_value)

  #Storing the list of In_Degree and Out_Degree of the Graph G into respective variables
  Idegree = G.in_degree()
  Odegree = G.out_degree()

  #Initializing a list and adding all the nodes with In_Degree = 1 
  data = []
  for x in Idegree:
    if x[1] == 1:
      data.append(x[0])

  #Initializing a list and adding all the nodes with Out_Degree = 1
  data1 = []
  for y in Odegree:
    if y[1] == 1:
      data1.append(y[0])

  #Calculating number of nodes with In_Degree = 1 and storing it in a variable
  ID = len(data)

  #Calculating number of nodes with Out_Degree = 1 and storing it in a variable
  OD = len(data1)

  #Calculating the R_in and R_out value used for the graph for each day which is used to describe the dynamics of system in the research paper.
  R_in = np.log(ID)/np.log(MaxIn)
  R_out = np.log(OD)/np.log(MaxOut)

  #Storing all these values in a tuple
  content = (R_in,R_out,ID,OD,MaxIn,MaxOut)
  #Appending the tuple in a sequence according to their date.
  CompleteDetails.append(content)

#Creating a dataframe, and each column gives a certain analysis details. Each row represents a day. 
df2 = pd.DataFrame(CompleteDetails, columns=['R_in','R_out','N1_in','N1_out','MaxInDegree','MaxOutDegree'])

#Saving the dataframe into a csv file named "CompleteData".
df2.to_csv(r"D:\\ERC20DATASET\\analysis\\CompleteData.csv", index=False)