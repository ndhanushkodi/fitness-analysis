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
from sklearn.cross_validation import train_test_split


df =pd.read_table(r'C:\Users\jmorris\Documents\Classes_Spring_2015\Data_Science\FitnessKeeper\FitnessData_2014.tsv', sep='\t')
#df.info()
print (df['age'].values)
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

umean = a.mean()
umeandict = umean.to_dict()
listOfUserId = umeandict['age'].keys()

#umean2 = umean['userid']
#print (umean2)
#print (umean2.shape)

train_data = df.values
#print (train_data)

"""
a_train, a_test = train_test_split(train_data, test_size=0.33, random_state=42)
print (a_train.shape)
print (a_test.shape)
a_train_df = pd.DataFrame(data=a_train)
print (a_train_df.dtypes)
#a_train_user = a_train_df.groupby('0')
#print (a_train_user.shape)
"""
a = df[df.genderNum==0].index


#print (a)
#print (np.random.choice(df.index.values, 100))

def createsEstimation():
    values =[]
    for i in range(1000):
        rows = np.random.choice(df.index.values, 100)
        sampled_df = df.ix[rows]
        values.append(sampled_df['distance_mi'].mean())
    return values
"""
def RMSE(estimates, actual):
    e2 = [(estimate-actual)**2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)
    
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

"""
plt.scatter(a['age'].mean(), a['distance_mi'].mean(),alpha=0.05)
plt.show()
"""

#print a.corr()
#print np.corrcoef(a['age'].mean(), a['distance_mi'])[0, 1]
