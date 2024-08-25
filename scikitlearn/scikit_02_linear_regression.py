# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:09:06 2020

@author: vaghajan
"""
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import seaborn as sns


data_df = pd.read_csv ('Advertising.csv', index_col = 0)
# visualize the relationship between the features and the response using scatterplots
sns.pairplot(data_df, x_vars=['TV','radio','newspaper'], y_vars='sales', size=7, aspect=0.7, kind='reg')

''' split the data '''
X = data_df[['TV', 'radio', 'newspaper']]
y = data_df['sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

''' Linear regression '''
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X_train, y_train)
# print the intercept and coefficients
print('Tetha0 : {}\n'.format(linreg.intercept_))
print(*['Theta'+str(i+1)+'='+str(co)+'\n' for i,co in enumerate(linreg.coef_)])
# pair the feature names with the coefficients
print(*list(zip(['TV','radio','newspaper'], linreg.coef_)))
print ('\n\n\n')
# make predictions on the testing set
y_pred = linreg.predict(X_test)

''' Model evaluation metrics for regression ...
•MAE is the easiest to understand, because it's the average error.
•MSE is more popular than MAE, because MSE "punishes" larger errors.
•RMSE is even more popular than MSE, because RMSE is interpretable in the "y" units
'''
from sklearn import metrics
# calculate MAE using scikit-learn
print ("mean_absolute_error = ")
print(metrics.mean_absolute_error(y_test, y_pred))

print ("\nmean_squared_error = ")
# calculate MSE using scikit-learn
print(metrics.mean_squared_error(y_test, y_pred))

# calculate RMSE using scikit-learn
print ("\nmean_squared_error = ")
print(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

''' Feature selection '''
X = data_df[['TV','radio']]
y = data_df.sales
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
linreg.fit(X_train, y_train)
y_pred = linreg.predict(X_test)
print(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


