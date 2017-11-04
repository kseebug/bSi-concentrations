import pandas as pd
import numpy as np
import csv
import glob

def read_csv(file_path):
	data = pd.read_csv(file_path,skiprows=26)
	data = data.dropna(subset=['Readings '])[['       Sample        ','Readings ']]
	data.columns = ['Sample','Absorbance']
	data.Sample = [x.strip() for x in data.Sample.tolist()]
	data = data[data.Sample!='blank']
	data = data[~data.Sample.isin(['0.25 uM','0.50 uM','1.50 uM'])]
	data = data[~data.Sample.isin([s for s in data.Sample.tolist() if 'std' in s])]
	print(data)

path =r'/Users/kseebug/Google Drive/Scripps/Barbeau/CCE/bSi/Raw data/' # use your path
allFiles = glob.glob(path + "*.csv")

for path_token in allFiles:
	read_csv(path_token)
	