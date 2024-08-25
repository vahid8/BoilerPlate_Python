# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 18:01:38 2020

•How can cross-validation be used for selecting tuning parameters, choosing between models, and selecting features?
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
''' Unpack the data bunch '''
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_name = iris.target_names

''' Print information '''
print('shape of the input matrix is : {}'.format(X.shape))
print('shape of the response matrix is : {}'.format(y.shape))
print('features are : ')
print (*[str(i+1)+'. '+name+'\n' for i,name in enumerate(feature_names)])
print('\n Targets are :')
print (*[str(i+1)+'. '+name+'\n' for i,name in enumerate(target_name)])

''' 1. KNN without K_fold_cross _validation '''
# use train/test split with different random_state values
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)
# check classification accuracy of KNN with K=5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

''' Steps for K-fold cross-validation
1.Split the dataset into K equal partitions (or "folds").
2.Use fold 1 as the testing set and the union of the other folds as the training set.
3.Calculate testing accuracy.
4.Repeat steps 2 and 3 K times, using a different fold as the testing set each time.
5.Use the average testing accuracy as the estimate of out-of-sample accuracy
'''
# simulate splitting a dataset of 25 observations into 5 folds
data = range(25)
kf = KFold(n_splits=5, shuffle=False).split(data)

# print the contents of each training and testing set
print('{} {:^61} {}'.format('Iteration', 'Training set observations', 'Testing set observations'))
for iteration, data in enumerate(kf, start=1):
    print('{:^9} {} {:^25}'.format(iteration, data[0], str(data[1])))
    
'''  Cross-validation recommendations
1.K can be any number, but K=10 is generally recommended
2.For classification problems, stratified sampling is recommended for creating the folds•Each response class should be represented with equal proportions in each of the K folds
• scikit-learn's cross_val_score function does this by default
'''

''' 2. KNN with K_fold_cross _validation for parameter tuning '''
from sklearn.model_selection import cross_val_score
# 10-fold cross-validation with K=5 for KNN (the n_neighbors parameter)
knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
# it does the splitting itself , score object is numpy array
print(scores)
# use average accuracy as an estimate of out-of-sample accuracy
print(scores.mean())
# search for an optimal value of K for KNN
k_range = list(range(1, 31))
k_scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
    k_scores.append(scores.mean())
print(k_scores)




# plot the value of K for KNN (x-axis) versus the cross-validated accuracy (y-axis)
plt.plot(k_range, k_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated Accuracy')

''' 2. K_fold_cross _validation for model selection between KNN and Logetic regression '''
# 10-fold cross-validation with the best KNN model
knn = KNeighborsClassifier(n_neighbors=20)
print(cross_val_score(knn, X, y, cv=10, scoring='accuracy').mean())
# 10-fold cross-validation with logistic regression
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
print(cross_val_score(logreg, X, y, cv=10, scoring='accuracy').mean())

''' 3. K_fold_cross _validation for feature selection '''
import pandas as pd
from sklearn.linear_model import LinearRegression
# read in the advertising dataset
data = pd.read_csv('data/Advertising.csv', index_col=0)
# create a Python list of three feature names
feature_cols = ['TV', 'Radio', 'Newspaper']

# use the list to select a subset of the DataFrame (X)
X = data[feature_cols]

# select the Sales column as the response (y)
y = data.Sales
# 10-fold cross-validation with all three features
lm = LinearRegression()
scores = cross_val_score(lm, X, y, cv=10, scoring='neg_mean_squared_error')
print(scores)

# fix the sign of MSE scores
mse_scores = -scores
print(mse_scores)

# convert from MSE to RMSE
rmse_scores = np.sqrt(mse_scores)
print(rmse_scores)

# calculate the average RMSE
print(rmse_scores.mean())

# 10-fold cross-validation with two features (excluding Newspaper)
feature_cols = ['TV', 'Radio']
X = data[feature_cols]
print(np.sqrt(-cross_val_score(lm, X, y, cv=10, scoring='neg_mean_squared_error')).mean())


'''  Improvements to cross-validation
Repeated cross-validation
•Repeat cross-validation multiple times (with different random splits of the data) and average the results
•More reliable estimate of out-of-sample performance by reducing the variance associated with a single trial of cross-validation

Creating a hold-out set
•"Hold out" a portion of the data before beginning the model building process
•Locate the best model using cross-validation on the remaining data, and test it using the hold-out set
•More reliable estimate of out-of-sample performance since hold-out set is truly out-of-sample

Feature engineering and selection within cross-validation iterations
•Normally, feature engineering and selection occurs before cross-validation
•Instead, perform all feature engineering and selection within each cross-validation iteration
•More reliable estimate of out-of-sample performance since it better mimics the application of the model to out-of-sample data

'''
# cross validation reduce the variance of single trial train-test split
# cross validation can be used for tunning parameters, selecting amon models
# or feature selection
# But cross validation is expenseive specially when the dataset is large
# or the model is slow to train
""" Grid search CV : More efficient parameter tuning using GridSearchCV """
# It does the parameter tunning using K-Fold crossvalidation
# But instead of manually writing a for loop to find parameter it
# does the job automatically
# Allows you to define a grid of parameters that will be searched using K-fold cross-validation
from sklearn.model_selection import GridSearchCV
# define the parameter values that should be searched
k_range = list(range(1, 31))
print(k_range)
# create a parameter grid: map the parameter names to the values that should be searched
param_grid = dict(n_neighbors=k_range)
print(param_grid)

# instantiate the grid
grid = GridSearchCV(knn, param_grid, cv=10, scoring='accuracy', return_train_score=False)

#You can set `n_jobs = -1` to run computations in parallel (if supported by your computer and OS)

# fit the grid with data
grid.fit(X, y)

# view the results as a pandas DataFrame
import pandas as pd
pd.DataFrame(grid.cv_results_)[['mean_test_score', 'std_test_score', 'params']]

# examine the first result
print(grid.cv_results_['params'][0])
print(grid.cv_results_['mean_test_score'][0])

# print the array of mean scores only
grid_mean_scores = grid.cv_results_['mean_test_score']
print(grid_mean_scores)

# plot the results
plt.plot(k_range, grid_mean_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated Accuracy')

# examine the best model
print(grid.best_score_)
print(grid.best_params_)
print(grid.best_estimator_)



"""   Searching multiple parameters simultaneously   """
# Example: tuning max_depth and min_samples_leaf for a DecisionTreeClassifier
# Could tune parameters independently: change max_depth while leaving min_samples_leaf at its default value, and vice versa
# But, best performance might be achieved when neither parameter is at its default value

# define the parameter values that should be searched
k_range = list(range(1, 31))
weight_options = ['uniform', 'distance']

# create a parameter grid: map the parameter names to the values that should be searched
param_grid = dict(n_neighbors=k_range, weights=weight_options)
print(param_grid)

# instantiate and fit the grid
grid = GridSearchCV(knn, param_grid, cv=10, scoring='accuracy', return_train_score=False) #initialization the object
grid.fit(X, y)

# view the results
pd.DataFrame(grid.cv_results_)[['mean_test_score', 'std_test_score', 'params']]

# examine the best model
print(grid.best_score_)
print(grid.best_params_)

# train your model using all data and the best known parameters
knn = KNeighborsClassifier(n_neighbors=13, weights='uniform')
knn.fit(X, y)

# make a prediction on out-of-sample data
knn.predict([[3, 5, 4, 2]])

# shortcut: GridSearchCV automatically refits the best model using all of the data
grid.predict([[3, 5, 4, 2]])


"""   Reducing computational expense using RandomizedSearchCV   """
#- Searching many different parameters at once may be computationally infeasible
#- `RandomizedSearchCV` searches a subset of the parameters, and you control the computational "budget"
from sklearn.model_selection import RandomizedSearchCV
# specify "parameter distributions" rather than a "parameter grid" for only continus parameters not discrete parameters like K
param_dist = dict(n_neighbors=k_range, weights=weight_options)
# n_iter controls the number of searches
rand = RandomizedSearchCV(knn, param_dist, cv=10, scoring='accuracy', n_iter=10, random_state=5, return_train_score=False)
rand.fit(X, y)
pd.DataFrame(rand.cv_results_)[['mean_test_score', 'std_test_score', 'params']]
# examine the best model
print(rand.best_score_)
print(rand.best_params_)
# run RandomizedSearchCV 20 times (with n_iter=10) and record the best score
best_scores = []
for _ in range(20):
    rand = RandomizedSearchCV(knn, param_dist, cv=10, scoring='accuracy', n_iter=10, return_train_score=False)
    rand.fit(X, y)
    best_scores.append(round(rand.best_score_, 3))
print(best_scores)



