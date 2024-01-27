
#First Question.
class Employee:
    employee_count = 0
    total_salary = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department

        Employee.employee_count += 1
        Employee.total_salary += salary

    # show_emp_info funtion to display emplopyee information.
    def show_emp_info(self):
        print("Name:", self.name, "Family:", self.family, "Salary:", self.salary, "Department:", self.department)

    
    # average_salary to calculate average salary of employees.
    def average_salary():
        return Employee.total_salary / max(Employee.employee_count, 1)



class FulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        super().__init__(name, family, salary, department)
    
    def display_fulltime_info(self):
     print("Full-time Employee Class Member Function.")


# Create instances of Employee class.
emp1 = Employee("Javeed Ather", "Ather Family", 50000, "HR")
emp2 = Employee("Ranadheer Bolli", "Bolli Family", 60000, "Finance")

# Create instances of FulltimeEmployee class.
fulltime_emp1 = FulltimeEmployee("Shirish Reddy", "Reddy Family", 70000, "IT")
fulltime_emp2 = FulltimeEmployee("Shabarish Guntur", "Guntur Family", 80000, "IT")

# Calling member function of Employee Class.
emp1.show_emp_info()
emp2.show_emp_info()

# Calling the average_salary function
average_salary = Employee.average_salary()
print("Average Salary", average_salary)

# Calling the show_emp_info function of Employee class.
fulltime_emp1.show_emp_info()
fulltime_emp2.show_emp_info()

# Calling the member function of FulltimeEmployee class.
fulltime_emp2.display_fulltime_info()

