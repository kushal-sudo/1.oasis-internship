# -*- coding: utf-8 -*-
"""Iris csv.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HT5LFXZHBx0Jeg5zunlvmaNWgkHs14FN
"""

import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

from google.colab import files
upload = files.upload()

df = pd.read_csv('Iris.csv')
df.head()

df = df.drop(columns = ['Id'])
df.head()

df.info()

df.describe()

df['Species'].value_counts()

df.isnull().sum()

#histograms

df['SepalLengthCm'].hist()
plt.title('sepal lenght')

df['SepalWidthCm'].hist()
plt.title('Sepal width')

df['PetalLengthCm'].hist()
plt.title('petal length')

df['PetalWidthCm'].hist()
plt.title('petal width')

colors = ['orange', 'green', 'purple']
species = ['Iris-setosa','Iris-versicolor','Iris-virginica']

for i in range(3):
  x = df[df['Species'] == species[i]]
  plt.scatter(x['SepalLengthCm'],x['SepalWidthCm'], c = colors[i], label = species[i])
  plt.xlabel('sepal lenght')
  plt.ylabel('sepalwidht')
  plt.legend()

for i in range(3):
  x = df[df['Species'] == species[i]]
  plt.scatter(x['PetalLengthCm'],x['PetalWidthCm'], c = colors[i], label = species[i])
  plt.xlabel('petal length')
  plt.ylabel('petal width')
  plt.legend()

for i in range(3):
  x = df[df['Species'] == species[i]]
  plt.scatter(x['SepalLengthCm'], x['PetalLengthCm'], c = colors[i], label = species[i])
  plt.xlabel('sepal length')
  plt.ylabel('petal length')
  plt.legend()

for i in range(3):
  x = df[df['Species'] == species[i]]
  plt.scatter(x['SepalWidthCm'],x['PetalWidthCm'], c = colors[i], label = species[i])
  plt.xlabel('sepal width')
  plt.ylabel('petal width')
  plt.legend()

"""correlation matrix"""

df.corr()

corr = df.corr()
fig,  ax  = plt.subplots(figsize = (3,4))
sns.heatmap(corr, annot=True, ax=ax)

sns.pairplot(df, hue ='Species',markers='*')
plt.show()

"""label encoding

"""



from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

df['Species'] = le.fit_transform(df['Species'])
df.head()

"""model training




"""

from sklearn.model_selection import train_test_split
#train - 70
#test  - 30
x = df.drop(columns = ['Species'])
y = df['Species']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30)

#logistic regression

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

#model training
model.fit(x_train, y_train)

print("accuracy:",model.score(x_test, y_test)*100)

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()

model.fit(x_train, y_train)

model.score(x_test, y_test)*100

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(x_train, y_train)

model.score(x_test, y_test)*100

