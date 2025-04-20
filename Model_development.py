from Splitting_dataset import train_indices
from Splitting_dataset import test_indices

from sklearn.linear_model import SGDClassifier

X_train = train_indices[::8]
y_train = train_indices[:9]
X_test = test_indices[::8]
y_test = test_indices[:9]

# Machine Learning with Linear Regression
lin_reg = SGDClassifier()
lin_reg.fit(train_data, train_label)

