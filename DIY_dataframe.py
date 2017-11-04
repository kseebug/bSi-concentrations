import pandas as pd
import numpy as np
import csv
import glob

def read_csv(file_path): # defining fxn to concatenate data
	data = pd.read_csv(file_path,skiprows=26) # removes the first 26 rows
	data = data.dropna(subset=['Readings '])[['       Sample        ','Readings ']] # removing NaNs
	data.columns = ['Sample','Absorbance'] # changes names of columns
	data.Sample = [x.strip() for x in data.Sample.tolist()] # strips blanks from strings
	data = data[data.Sample!='blank'] # removing blanks
	data = data[~data.Sample.isin(['0.25 uM','0.50 uM','1.50 uM'])] # removing stds
	data = data[~data.Sample.isin([s for s in data.Sample.tolist() if 'std' in s])] # removing stds
	print(data)

path =r'/Users/kseebug/Google Drive/Scripps/Barbeau/CCE/bSi/Raw data/' # use your path
allFiles = glob.glob(path + "*.csv") # i have no fucking clue. not a map of the world

for path_token in allFiles:
	read_csv(path_token) # using the fxn
