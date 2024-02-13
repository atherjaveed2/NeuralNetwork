# Importing the required libraries.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

# Loading the dataset from a CSV file.
glass_data = pd.read_csv("glass.csv")

# Separating features (X) and the target variable (y).
X = glass_data.drop('Type', axis=1)
y = glass_data['Type']

# Splitting the dataset into training and testing sets. using train_test_split method.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing the Naive Bayes classifier.
naive_bayes = GaussianNB()

# Training the classifier on the training data.
naive_bayes.fit(X_train, y_train)

# Calculating and printing the training accuracy.
training_accuracy = round(naive_bayes.score(X_train, y_train) * 100, 2)
print("Training Accuracy:", training_accuracy)

# Predicting the target variable for the testing data.
y_pred = naive_bayes.predict(X_test)

# Calculating and printing the testing accuracy.
testing_accuracy = accuracy_score(y_test, y_pred)
print("Testing Accuracy:", testing_accuracy)

# Generating and printing the classification report for the testing data.
class_report = classification_report(y_test, y_pred)
print("Classification Report using Naive Bayes")
print(class_report)
