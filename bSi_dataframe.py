import pandas as pd
import numpy as np
file_token = '/Users/kseebug/Google Drive/Scripps/Barbeau/CCE/bSi/bSi_silica_data_sheet2.xlsx'
a = pd.read_excel(file_token,usecols=19,sheet_name='data sheet')
conversion_list = {'A':1.375,'B':2.625,'C':5.965909091,'D':1,'E':1.875,'F':6.25,'G':9375,'H':5.25,'I':7.5}
poly_a = -6.84578043712098E-06 #this is a variable in the polynomial
poly_b = 0.0114955100658752
poly_c = 0.000423122081959965
b = a.dropna(subset=['Dilution'])
for row in b.iterrows():                                   
	absorb = row[1].Absorbance                                         
	polynomial = np.array([poly_a,poly_b,poly_c-absorb])
	root = (-poly_b+np.sqrt(poly_b**2-4*poly_a*(poly_c-absorb)))/(2*poly_a)
	dil = root * 5/row[1]['Volume (mL)']*conversion_list[row[1].Dilution]
	print(dil)