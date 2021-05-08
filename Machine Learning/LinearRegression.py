#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  8 11:25:13 2021

@author: sysad
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, linear_model, metrics

#%% Read_load_data
df = pd.read_csv("/home/sysad/Desktop/akshay/Histopathology/Programs/100DaysofCode/insurance.csv")
df.isnull().sum()
df.info()

#seperating categorical and continuous variables
cat = []
cont = []
for col in df.columns:
    if df[col].dtype == 'object':
        cat.append(col)
    else:
        cont.append(col)
print("Catagorical variables are: ", cat)
print("Continuous variables are: ", cont)
#%%Plots    
sns.countplot(df.smoker, hue= df.sex)
plt.show()

df.groupby(['smoker'])['sex'].value_counts()

plt.figure(figsize=(8,6))
sns.barplot(x= df.region, y= df.charges, hue= df.smoker )
plt.show()

sns.distplot(df[df['smoker'] == 'yes'].charges, color='r')
plt.show()

sns.distplot(df[df['smoker']=='no'].charges, color='b')
plt.show()
'''we can see that those who smokes incus more charages compared to those who do not'''

sns.scatterplot(x=df.age, y= df.charges, hue=df.smoker)
plt.show()

sns.violinplot(x=df.region, y= df.charges, hue=df.smoker, split=True)
plt.show()

sns.histplot(x=df.bmi)
plt.show()

sns.distplot(x=df.bmi)
plt.show()

plt.figure(figsize=(8,8))
sns.jointplot(x = df.bmi, y = df.charges, hue = df.children)
plt.show()

plt.figure(figsize=(8,8))
sns.jointplot(x = df.bmi, y = df.charges, hue = df.smoker)
plt.show()

plt.figure(figsize=(8,6))
sns.scatterplot(x = df.bmi, y=df.charges, hue = df.smoker)
plt.show()

#%% Train_Test
'''conversion of categorical value to continuos values using LABEL ENCODING'''

for col in df.columns:
    encoder = preprocessing.LabelEncoder()
    encoder.fit(df[col])
    df[col] = encoder.transform(df[col])
df.describe()

##Plotting correlation matrix
plt.figure(figsize=(6,6))scaler = preprocessing.MinMaxScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_train) 
sns.heatmap(df.corr(), annot=True)
plt.show()
'''Charges are dependent on both age and smoking habit of a person '''


X = df.drop(['charges'], axis=1)
Y = df['charges']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.75, random_state=0, shuffle=True)


'''minmaxscaler() is used to to scale and trnaslate each feature individually s.t. it is
   in given range(usually between zero and one). This is an alternative o zero mean , unit variance scaling.
   x_std = (x - x.min(axis=0))/(x.max(axis=0) - x.min(axis=0))
   x_sclaed = x_std * (max - min) + min'''
scaler = preprocessing.MinMaxScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test) 

linreg = linear_model.LinearRegression()
linreg.fit(X_train, Y_train)
Y_pred = linreg.predict(X_test)
   
print("Linear regression score :", linreg.score(X_test, Y_test))
print("Mean square error is :", metrics.mean_squared_error(Y_test, Y_pred))
print("mean absolute error :", metrics.mean_absolute_error(Y_test, Y_pred))
