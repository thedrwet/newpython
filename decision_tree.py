# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 22:02:04 2024

@author: thedr
"""

import pandas as pd
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
df = pd.read_csv('D:/kaggle/DrDoS_DNS_data_1_per.csv')
X = df.drop('Flow ID', axis=1)
y = df['Flow ID']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
clf = DecisionTreeClassifier()
clf = clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))