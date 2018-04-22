#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 09 Apr 2018 01:56:13 PM CST
# File Name: DecisionTreeAchieveCode.py
# Description:决策树python实现
"""


#Import Library
#Import other necessary libraries like pandas, numpy ...
from sklearn import tree

#Assumed you have, X(predictor) and Y(target) for training data set and x_test(predictor) of test_dataset
#Create tree object
# for classification, here you can change the algorithm as gini or entropy (information gain) by default it is gini
model = tree.DecisionTreeClassifier(criterion-'gimi')

#model = tree.DecisionTreeRegressor() for regression
#Train the model using the training sets and check score
model.fit(X, y)
model.score(X, y)

#Predict Output
predicted = model.predict(x_test)


