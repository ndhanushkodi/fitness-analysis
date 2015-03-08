# -*- coding: utf-8 -*-
"""
Created on Fri Feb 06 12:00:51 2015

@author: jmorris
"""
import random
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import thinkstats2
import thinkplot
from sklearn import cross_validation


#df =pd.read_table(r'C:\Users\jmorris\Documents\Classes_Spring_2015\Data_Science\FitnessKeeper\FitnessData_2014.tsv', sep='\t')
df=pd.read_table('/home/ndhanushkodi/SOPHCLASSES/DataSci/FitnesskeeperData/FitnessData_2014.tsv', sep='\t')

#df.info()
df['genderNum'] = df['gender'].map( {'F': 0, 'M': 1} ).astype(int)
"""
print "MEAN VALUES"
print "Age: " + str(df['age'].mean())
print "Distance_mi: " + str(df['distance_mi'].mean())
print "Duration_mi: " + str(df['duration_min'].mean())
print "Trips_before: " + str(df['trips_before'].mean())
print "Distance_before_mi: " + str(df['distance_before_mi'].mean())
print "Duration_before_min: " + str(df['duration_before_min'].mean())
print "Is_elite: " + str(df['is_elite'].mean())
"""

a= df.groupby('userid')






def createsEstimation():
    values =[]
    for i in range(1000):
        rows = np.random.choice(df.index.values, 100)
        sampled_df = df.ix[rows]
        values.append(sampled_df['distance_mi'].mean())
    return values

def RMSE(estimates, actual):
    e2 = [(estimate-actual)**2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)
    
def runEstimation():	
	samples = (createsEstimation())
	samples.sort()
	print("CI: ")
	print (samples[100])
	print (samples[900])
	print ("RMSE: ")
	print (RMSE(samples, df['distance_mi'].mean()))


plt.hist(samples)
plt.show()




"""
plt.scatter(a['age'].mean(), a['distance_mi'].mean(),alpha=0.05)
plt.show()
"""

#print a.corr()
#print np.corrcoef(a['age'].mean(), a['distance_mi'])[0, 1]
