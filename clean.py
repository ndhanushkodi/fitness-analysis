import pandas as pd
from pandas import DataFrame as DF
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import normal
import thinkstats2
import thinkplot

#df=pd.read_table('/home/ndhanushkodi/SOPHCLASSES/DataSci/FitnesskeeperData/FitnessData_2014.tsv', sep='\t')

"""
The actual useful function of this file. 
So you can run 1 line of code to clean up 
the data before running any analysis. 
Cleans data by adding pace column and cleaning by
distance, duration, and pace.
"""
def clean_data(df):
	df['pace'] = df.duration_min/df.distance_mi
	rw = df[(df['distance_mi']>0.5) & (df['distance_mi']<30)]
	rw = rw[(rw['duration_min']>10) & (rw['duration_min']<360)]
	rw = rw[(rw['pace']>3) & (rw['pace']<30)]
	return rw


"""
Does the groupby user
"""
def org_by_user(df):
	u = df.groupby('userid')
	return u

def means(u):
	return u.mean()

"""
Not really necessary to make this happen in a separate
python file. Just testing modules. 
"""
def trips_before_histogram(trips_before):
	plt.hist(trips_before, range=(0,600),bins=100)
	plt.title("Trips_before_histogram")
	plt.xlabel("Trips_before")
	plt.ylabel("Frequency")
	plt.show()


if __name__ == "__main__":
	clean_data()