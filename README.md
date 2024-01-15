# NeuralNetwork
 Assignment 1 of Neural Network and Deep Learning.

 **Student Information:**
 Name: Fnu M A Javeed Ather

 Student Id: 700761692

 Email : lxm16920@ucmo.edu

 CRN Number: 22317

**Githublink:** https://github.com/atherjaveed2/NeuralNetwork

 **Video Link:** https://drive.google.com/file/d/1X5jwh6WcDhPW9mc5YVmJL_HKX5xqXo1Z/view?usp=share_link

 **Description:** This repository consists of python code for four coding questions of Assingment 1 of Neural Network and Deep Learning.
 
 **Questions and Answers:**

**Question 1A.** Input the string “Python” as a list of characters from console, delete at least 2 characters, reverse the resultant string and print it.
**Answer.** As given in the question we have initialized an empty list(`char_list`) for storing the list of characters entered by the user from console and also initialized an empty string(`res_string`) for storing the reversed list of characters as a string. Next we have written logic for storing the input list of characters for that we have used a while loop and allow user to enter each character at a time and insert each character into our empty list(`char_list`) and if the user presses `Enter` button without entering a character then the if condition satisfies and the while loop breaks and process of entering input from console stops. Next we have written logic for removing atleast two characters (two starting characters as per our logic). In this logic first we are checking whether the length of `char_list` is 2 characters or not. If the length of input char list is less than 2 then we are asking user to enter the atleast two characters and if the legnth of input char list is 2 or greater than 2 we are removing the first two characters from the list and reversing the list using `slicing` and storing it it new variabe called `output_list`. Later we are are converting the `output_list` into a string using `join` method and printing it as Output of the code.

**Question 1B.** Take two numbers from user and perform at least 4 arithmetic operations on them.
A**nswer.** As given in the question we have taken two variables `first_number` , `second_number` to store the input numbers entered by the user we have used float type as we don't know the user will enter only integers he/she may enter only decimals also. Later we are performing four arithematic operations on them `Addition`, `Mulliplication`, `Substraction` and `Division` and printing the output as given in the question.

**Question 2.** Write a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’.
**Answer.** As given in the question we are accepting a sentence from the user as input and storing it in variable called `input_str`. Then we convert the input sentence into array of strings using `split` method and store in a varible called `array_of_strings`. Next we have initialized an empty string `output_str` for storing the output sentence. Later we have written logic for replacing the word `python`
 with `pythons` by running a for loop over the `array_of_strings` and checking if at the particular index if we have the word `python` then replace it with `pythons` and appending the current word to the output string(`out_str`). This process continues untill the for loop range is exceeds the length of `array_of_strings`. At the end we print the `output_str` a sentence where every `python` word is replaced with `pythons`.

 **Question 3.** Use the if statement conditions to write a program to print the letter grade based on an input class score. Use the grading scheme we are using in this class.
**Answer.** As given in the question we are taking an integer or decimal as input from the user and storing in variable `class_score`. Later we have written logic for calculating grade using if else condition. We have used the below grading requirememt for calculation grade.
Grading Scale
Percent (%)    Grade
 90-100        A
 80-89         B
 70-79         C
 60-69         D
 0-59          F

**Technology Used:** Python3

**Usage:** Install any python idle and clone this repository and run this command Ex: python3 file_name.py to run each file.



