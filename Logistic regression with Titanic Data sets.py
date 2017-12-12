import pandas as pd
%pylab inline
# Reading Titanic Data
df = pd.read_csv("train.csv")
# Make use of all columns in the csv file 
df = pd.columns
X = pd.DataFrame()
X['sex'] = df ['sex']
X['age'] = df ['Age']
X['Survived'] = df['Survived']
X = X.dropna(axis=0)
y= X['Survived']
X=X.drop(['Survived'],axis=1)
pd.get_dummies(X.sex)
X['Sex'] = pd.get_dummies(X.sex)['female']
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X= Scaler.fit_transform
# Build Test and Make Training Sets
X_train, X_test, y_train, y_test = train_test_split(X. y, test_size=0.2, random_state=42)
# Modeling
def base_rate_model(X):
	y = np.zeros(X.shape[0])
	return y
y_base_rate = base_rate_model(X_test)
from sklearn.metrics import accuracy_score
print "base rate accuracy is %2.2f"% accuracy_score(y_test, y_base_rate)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(penalty'l2',C=1)
print"Logistic accuracy is %2.2f" %accuracy_score(y_test,model.predict(X_test))
from sklearn.metrics import roc_auc_score
from sklearn.metrics import classification_report
Print "\nLogistic Model"
logit_roc_auc = roc_auc_score(y_test, model.predict(X_test))
print "Logistic AUC = %2.2f" % logit_roc_auc
print classification_report(y_test ,model.predict(X_test))