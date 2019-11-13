#!usr/bin/env/python3
'''
Gets the pandas dataframe and performs linear regression

'''
from dataClean import *
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import preprocessing
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression

def linearRegressionOneHot(data):
	# plt.plot(data.Mileage.values-np.mean(data.Mileage.values))
	# plt.show()
	X = pd.DataFrame(data.drop(['Price'],axis=1))
	y = pd.DataFrame(data['Price'])
	# print(X.head)
	model = LinearRegression()
	scores = []
	kfold = KFold(n_splits=3, shuffle=True, random_state=42)
	for i, (train, test) in enumerate(kfold.split(X, y)):
		model.fit(X.iloc[train,:], y.iloc[train,:])
		score = model.score(X.iloc[test,:], y.iloc[test,:])
		scores.append(score)
	print(scores)

def main():
    data = data_processor('Data/true_car_listings.csv')
    print("Received Clean Data")
    linearRegressionOneHot(data)


if __name__ == '__main__':
	main()