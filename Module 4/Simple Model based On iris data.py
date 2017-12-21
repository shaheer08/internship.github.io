from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation  import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import cPickle as pickle
import requests, json
# To See data 
# print iris.DESCR
iris = datasets.load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3)
rfc = RandomForestClassifier(n_estimators=100,n_jobs=2)
rfc.fit(X_train,y_train)
print "Accuracy =%0.2f" % accuracy_score (y_test,rfc.predict(X_test))
print classification_report(y_test, rfc.predict(X_test))
pickle.dump(rfc, open("iris_rfc.pkl", "wb"))

