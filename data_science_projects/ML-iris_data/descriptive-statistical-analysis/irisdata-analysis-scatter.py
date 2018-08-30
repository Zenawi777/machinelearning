# This script import iris data from a file and parses the data for analysis 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Import data from a file
df = pd.read_csv('iris-data-copy.txt',header=0,sep=',',usecols=range(4))



#Plot of the data

# Making a grid of a figure window
grid_size=(1,3)
colors=np.random.rand(len(df))

# Scatter plot of the first column against the second 
_ = plt.subplot2grid(grid_size,(0,0))
scatter_plot=plt.scatter(df['5.1'],df['3.5'],c=colors)

# Scatter plot of the first with respect to third column
_ = plt.subplot2grid(grid_size,(0,1))
scatter_plot=plt.scatter(df['5.1'],df['1.4'],c=colors)

# Scatter plot of the first with respect to fourth column
_ = plt.subplot2grid(grid_size,(0,2))
scatter_plot=plt.scatter(df['5.1'],df['0.2'],c=colors)

plt.show() # Displaying the scatter plot
