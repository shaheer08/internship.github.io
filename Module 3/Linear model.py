import numpy as np
import pandas as pd
from sklearn import datasets 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import linear_model


# To See data 
# print iris.DESCR
iris = datasets.load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y)
# model
model = linear_model.LinearRegression()
model = model.fit(X_train, y_train)

# predictions
predictions = model.predict(X)

print("Predicted\tTrue Value")
for i in range(0,len(predictions)):
    print("%.3f\t\t%f" % (predictions[i], y_test[i]))
plt.scatter(X_test,y_test, color='black')
plt.plot(X_test, predictions, color='red', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()