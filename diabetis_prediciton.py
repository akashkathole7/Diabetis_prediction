# -*- coding: utf-8 -*-
"""Diabetis_prediciton.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10TZKrhnPNfYVCzySUmFcJrxIJ50Hq8dz
"""

# Commented out IPython magic to ensure Python compatibility.
# import depedencies 
import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
# %matplotlib inline

# load the data 
dataset = pd.read_csv('/content/diabetes.csv')

# print first five rows on data for understnding 
dataset.head()

# print shape of data 
dataset.shape

# check any missing value in dataset
dataset.isnull().sum()

# check types of data 
dataset.dtypes

# get more informatin from data 
dataset.info()

# describe data
dataset.describe(include = 'all')

# visualize the data 
plt.hist(x = dataset,bins = 25)
plt.title('histogram of dataset')
plt.show()

# checking the relation with data 
correlation = dataset.corr()

sns.heatmap(correlation,annot = True,cmap = 'Blues')
plt.title('relation')
plt.show()

X = dataset.drop(columns = ['Outcome'],axis = 1)
Y = dataset['Outcome']

# let split data into training and testing 
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,random_state= 2)

# selecting the model 
model = SVC()

# fitting the model 
model.fit(X_train,Y_train)

train_predict = model.predict(X_train)
test_predict = model.predict(X_test)

#checking the accuracy of model 
accuracy_score(Y_train,train_predict)

accuracy_score(Y_test,test_predict)

input_data = [1,89,66,23,94,28.1,0.167,21]
in_array_data = np.array(input_data)
reshape_data = in_array_data.reshape(1,-1)
prediction = model.predict(reshape_data)
if prediction[0]==1:
  print('patience have a diabetis')
else :
  print('patience have a no diabetis')