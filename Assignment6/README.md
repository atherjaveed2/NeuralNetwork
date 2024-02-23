# NeuralNetwork
 Assignments of NeuralNetworks

 Student Information: 
 Name: Fnu M A Javeed Ather
 Student Id: 700761692
 Email : lxm16920@ucmo.edu
 CRN Number: 22317

 Githublink: https://github.com/atherjaveed2/NeuralNetwork/tree/main/Assignment6

 Video Link: https://drive.google.com/file/d/1L6XJD-5HUd8bd_m3NxLmrLWOCQJZ4Qel/view

**Question 1.** 
Use Case Description:
Predicting the diabetes disease
Programming elements:
Keras Basics
In class programming:
1. Use the use case in the class:
a. Add more Dense layers to the existing code and check how the accuracy changes.
1. Change the data source to Breast Cancer dataset * available in the source code folder and make 
required changes. Report accuracy of the model.
2. Normalize the data before feeding the data to the model and check how the normalization change 
your accuracy (code given below)
from sklearn.preprocessing import StandardScaler sc = StandardScaler()
Breast Cancer dataset is designated to predict if a patient has Malignant (M) or Benign = B cancer



**Question 2.** 
Use Image Classification on the hand written digits data set (mnist)
1.Plot the loss and accuracy for both training data and validation data using the history object in the 
source code.
2.Plot one of the images in the test data, and then do inferencing to check what is the prediction of 
the model on that single image.
3.We had used 2 hidden layers and Relu activation. Try to change the number of hidden layer and 
the activation to tanh or sigmoid and see what happens.
4.Run the same code without scaling the images and check the performance?


**Answer.** 
For both questions the code is written using the inbuilt library functions of keras, pandas and scikit-learn of python and for referece I have added the comments in the code itself.

