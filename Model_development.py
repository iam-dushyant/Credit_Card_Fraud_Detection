from Splitting_dataset import train_indices
from Splitting_dataset import test_indices

from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix

X_train = train_indices.iloc[:,:8]
y_train = train_indices.iloc[:,9]
X_test = test_indices.iloc[:,:8]
y_test = test_indices.iloc[:,9]

# Machine Learning with Linear Regression
classifier = SGDClassifier()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

# Checking prediction using Confusion Matrix
conf_mat = confusion_matrix(y_train, y_pred)