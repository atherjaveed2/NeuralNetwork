# NeuralNetwork
 Assignments of NeuralNetworks

 Student Information: 
 Name: Fnu M A Javeed Ather
 Student Id: 700761692
 Email : lxm16920@ucmo.edu
 CRN Number: 22317

 Githublink: https://github.com/atherjaveed2/NeuralNetwork/tree/main/Assignment3

 Video Link: https://drive.google.com/file/d/1pjL_YR1OnqHEefhDNpPS_UcF76TXQf9l/view?usp=sharing

**Question 1.** 1. Create a class Employee and then do the following
• Create a data member to count the number of Employees
• Create a constructor to initialize name, family, salary, department
• Create a function to average salary
• Create a Fulltime Employee class and it should inherit the properties of Employee class
• Create the instances of Fulltime Employee class and Employee class and call their member functions.

**Answer.** 
The base class, the `Employee` class, has properties like name, family, department, and pay. The cumulative wage (`total_salary`) and the total number of employees (`employee_count`) are also tracked using class-level variables. The class methods consist of a static method called average_salary that determines the average salary for all workers, an initializer called `__init__` that sets instance attributes and updates the class-level variables, and a method called `show_emp_info` that displays data about individual employees.

Moreover, the `Employee` class is the parent of the `FulltimeEmployee` class, which inherits its methods and properties. It adds a new method (`display_fulltime_info`) that is only available to full-time workers. To show the functionality, instances of both classes are made and their methods are called.

**Question 2.** Using NumPy create random vector of size 20 having only float in the range 1-20. Then reshape the array to 4 by 5
Then replace the max in each row by 0 (axis=1)   (you can NOT implement it via for loop)
**Answer.**  
NumPy is used to generate a random vector of size 20, where each element is a floating-point number within the range of 1 to 20. The generated random vector is then reshaped into a 4x5 matrix (a 2D array with 4 rows and 5 columns).Following the array's reshaping, argmax(axis=1) is used to determine the column indices of each row's maximum values. Next, it replaces each row's maximum value with 0 using NumPy's clever indexing (reshaped_array[np.arange(4), reshaped_array.argmax(axis=1)]).



