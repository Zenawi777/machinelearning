# This script import iris data from a file and parses the data for analysis 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import data from a file
df = pd.read_csv('iris-data-copy.txt',header=0,sep=',',usecols=range(4))

# Statistical analysis of data

# getting the minimum
mn=min(df)
print(mn)

# getting the maximum
mx=max(df)
print(mx)

# Computing the standard deviation
sd=df.std(axis=None,level=None,ddof=1)
print(sd)

# Computing the mean
mnn=df.mean(axis=None,level=None)
print(mnn)


# Analysing data for hisogram plot

# Capturing the first 50 rows of the data (Those data are of the same species)
sep=df.iloc[0:49]

# Getting the first column of the data
ind1=sep['5.1']

# Getting the second column of the data
ind2=sep['3.5']

# Getting the third column of the data
ind3=sep['1.4']

# Getting the fourth column of the data
ind4=sep['0.2']

# Ploting the data

# Spliting a graph into four grids
grid_size=(2,2)


# Ploting the first column of the data
_=plt.subplot2grid(grid_size,(0,0))
_=plt.hist(ind1)

# Ploting the second column of the data
_=plt.subplot2grid(grid_size,(0,1))
_=plt.hist(ind2)

# Ploting the third column of the data
_=plt.subplot2grid(grid_size,(1,0))
_=plt.hist(ind3)

# Ploting the fourth column of the data
_=plt.subplot2grid(grid_size,(1,1))
_=plt.hist(ind4)


#Displaying the whole data set in a single sindow
plt.show()
