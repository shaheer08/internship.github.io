from sklearn import datasets

import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression

# Loading iris data set 
iris = datasets.load_iris()

X = iris.data[:,[2,3]]

Y = iris.target

# Here we use 30% of the data that denotes 0.3
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.3, random_state=0)


sc = StandardScaler()

sc.fit(X_train)


X_train_std = sc.transform(X_train)

X_test_std = sc.transform(X_test)

Ir =LogisticRegression(C=1000.0, random_state=0)

Ir.fit(X_train_std,Y_train)


 
print (X_test_std[0,:])


print (Ir.predict_proba(X_test_std[30,:].reshape(1,-1)))


print (Ir.predict_proba(X_test_std[0,:].reshape(1,-1)))

