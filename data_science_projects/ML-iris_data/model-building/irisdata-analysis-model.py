# This script import iris data from a file and parses the data for analysis 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Import data from a file
df = pd.read_csv('iris-data-copy.txt',header=0,sep=',',usecols=range(4))





