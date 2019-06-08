#!/usr/bin/env python
import os
import sys
import json
import pandas as pd

from sklearn import tree
from sklearn.model_selection import StratifiedShuffleSplit

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


def preprocess(train):
    labels = train.iloc[:, 8:9].values
    train = train.drop(['diagnostic'], axis=1)
    return train, labels


def predict(patient):
    df = pd.read_csv('reg.csv', delimiter=';')
    X, y = preprocess(df)
    sss = StratifiedShuffleSplit(10, test_size=0.3, random_state=0)
    for train_index, test_index in sss.split(X, y):
        X_train, X_test = X.values[train_index], X.values[test_index]
        y_train, y_test = y[train_index], y[test_index]
    clf = tree.DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    pacientData = patient.split(",")
    test = [pacientData]
    pred = clf.predict(test)[0]
    print(pred)
    data = {}
    data['prediction'] = pred
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)


def cie9(code):
    with open("cie9.csv", 'r') as file:
        for line in file:
            if code in line:
                return line.split(";")
