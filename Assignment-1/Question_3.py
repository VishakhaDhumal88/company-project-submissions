# 1. Struct equivalent in Python using Class
# A class groups related attributes of an employee into one logical unit
class Employee:
    def __init__(self, emp_id, first_name, last_name, salary, department):
        self.emp_id = emp_id              # Number: Unique employee ID
        self.first_name = first_name      # String: Employee's first name
        self.last_name = last_name        # String: Employee's last name
        self.salary = salary              # Number: Employee's salary
        self.department = department      # String: Department name

    def __repr__(self):
        return f"Employee({self.emp_id}, {self.first_name} {self.last_name}, Dept: {self.department})"

# Creating an example Employee object
emp1 = Employee(101, "Alice", "Smith", 70000, "Marketing")

# 2. List
# A list can store multiple employees or just attributes of an employee
# Example: List of employee names (strings)
employee_names = ["Alice", "Bob", "Charlie"]

# List of Employee objects to represent multiple employees
employee_list = [
    emp1,
    Employee(102, "Bob", "Johnson", 80000, "Finance"),
    Employee(103, "Charlie", "Williams", 75000, "IT")
]


# 3. String
# strings store textual data such as employee names, departments, roles
employee_name = "Diana Prince"        # Individual string for name
department_name = "Human Resources"   # Department as string


# 4. Number
# Numbers represent numeric data like employee IDs, salaries, ages
employee_id = 104
employee_salary = 90000.50


# 5. Map (Dictionary in Python)
# Maps key-value pairs; great for representing employee data dynamically
# Keys are attribute names, values are the actual data
employee_dict = {
    "emp_id": 105,
    "first_name": "Eve",
    "last_name": "Davis",
    "salary": 72000,
    "department": "Research"
}

# Dictionary mapping employee IDs to their records (fast lookup by ID)
employees_map = {
    101: emp1,
    102: employee_list[1],
    103: employee_list[2],
    105: employee_dict
}


# 6. Array
# Python does not have built-in fixed-size arrays, but lists are typically used
# However, the `array` module can be used for efficient numeric arrays
import array

# Array of employee salaries (floats)
salary_array = array.array('f', [70000.0, 80000.0, 75000.0])


# 7. Set
# A set stores unique elements, useful for unique employee IDs or department names
unique_employee_ids = {101, 102, 103, 105}
unique_departments = {"Marketing", "Finance", "IT", "Research"}

# Adding a new employee ID (automatically avoids duplicates)
unique_employee_ids.add(106)

# Summary printouts to verify structure
print("Employee Object:", emp1)
print("List of Employee Names:", employee_names)
print("Employee Dictionary:", employee_dict)
print("Employee Map Lookup by ID 102:", employees_map[102])
print("Salary Array:", list(salary_array))
print("Unique Employee IDs Set:", unique_employee_ids)
print("Unique Departments Set:", unique_departments)

"""Explanation Summary:
Struct (Class): Encapsulates multiple related fields into a single employee entity — easy to manage and extend.
List: Holds ordered collections, useful for storing multiple employees or a list of attributes.
String: Holds text data such as employee names and departments.
Number: Numeric data like employee ID or salary.
Map (Dictionary): Flexible key-value storage for employee attributes; also great for fast lookup using unique keys.
Array: Efficient storage of same-type numeric data (e.g., salaries), though less commonly used than lists for general objects.
Set: Stores unique elements for quick membership tests and preventing duplicates (e.g., unique IDs or department names)."""