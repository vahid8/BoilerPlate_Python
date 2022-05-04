# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
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

''' create panda dataframe for understanding the data '''
data = np.zeros((X.shape[0],X.shape[1]+1))
data[:,:-1] = X
data[:,-1] = y
column_names = feature_names.copy()
column_names.append('response') 
data_df = pd.DataFrame(data, columns = column_names)

''' viuslaize data using seaborn '''
# To do

''' devide data into train and test '''
X_train,X_test,y_train,y_test = \
train_test_split (X,y,test_size = 0.4,random_state = 4)
# train and test set are always the same for model selection or parametr tunning !

''' logistic regresiion '''
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

lgreg = LogisticRegression(max_iter = 200) # Define the model

lgreg.fit (X_train,y_train) # fit using the train data
y_pred = lgreg.predict(X_test) # predict for test data
print(metrics.accuracy_score(y_test,y_pred)) #•Proportion of correct predictions


''' KNN classification '''
from sklearn.neighbors import KNeighborsClassifier

# Knn parameter tunning -> parameter is k (number of clusters)
# try k=1 through k =25 and record testing accuracy
k_range = range(1,26)
scores =list()
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit (X_train, y_train)
    y_pred = knn.predict (X_test)
    scores.append(metrics.accuracy_score(y_test,y_pred))
    
print(*scores)

# plot the relationhip between K and testing accuracy
plt.plot(k_range, scores)
plt.xlabel ('value of K for KNN')
plt.ylabel ('Testing Accuracy')

# selecting best k 
#Imortant : Make predictaions on out-of-sample data
knn = KNeighborsClassifier (n_neighbors = 6)
knn.fit (X,y)
knn.predict([[3,5,4,2]])
