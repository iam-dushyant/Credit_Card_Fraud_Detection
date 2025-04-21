from Splitting_dataset import train_indices
from Splitting_dataset import test_indices

from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

import seaborn as sns
import matplotlib.pyplot as plt

X_train = train_indices.iloc[:,[0, 2, 4, 5, 7, 8]]
y_train = train_indices.iloc[:,9]
X_test = test_indices.iloc[:,[0, 2, 4, 5, 7, 8]]
y_test = test_indices.iloc[:,9]

# Machine Learning with Linear Regression
classifier = SGDClassifier()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

# Checking prediction using Confusion Matrix and viewing it
conf_mat = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()

# Calculate accuracy score
accuracy = accuracy_score(y_test, y_pred) * 100
print(f"Accuracy: {accuracy:.5f}%")

# Looks like the accuracy for a 70/30 split is 99.73%, which is excellent!