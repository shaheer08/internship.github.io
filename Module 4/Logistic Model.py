import numpy as np
import pandas as pd
from sklearn.externals import joblib
from sklearn import datasets 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# To See data 
# print iris.DESCR
iris = datasets.load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3)
# model
model = LogisticRegression()
model = model.fit(X_train, y_train)
model_name = 'iris_model.pkl'
# model dumb
joblib.dump(model, model_name)
# predictions
predictions = model.predict(X)

print (Predictions)
