# Importing the required libraries.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset from CSV.
glass_data = pd.read_csv("glass.csv")

# Separating features (X) and target variable (y).
X = glass_data.drop('Type', axis=1)
y = glass_data['Type']

# Spliting dataset into training and testing sets using train_test_split method.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing linear SVM classifier.
svm = SVC()

# Training the linear SVM classifier.
svm.fit(X_train, y_train)

# Predicting on the testing set using linear SVM.
y_pred_svm = svm.predict(X_test)

# Calculating accuracy on training set.
training_accuracy = round(svm.score(X_train, y_train) * 100, 2)
print("Training Accuracy:", training_accuracy)

# Calculating accuracy score for linear SVM
accuracy_svm = accuracy_score(y_test, y_pred_svm)
print("Testing Accuracy:", accuracy_svm)

# Generating classification report.
class_report = classification_report(y_test, y_pred_svm, zero_division=1)
print("Classification Report using SVM method:")
print(class_report)
