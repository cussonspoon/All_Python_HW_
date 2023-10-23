class Name:
    def __init__(self, title, firstName, lastName):
        self.title = title
        self.firstName = firstName
        self.lastName = lastName

    def set_name(self, t, f, l):
        self.title = t
        self.firstName = f
        self.lastName = l

    def get_Full_Name(self):
        return f"{self.title} {self.firstName} {self.lastName}"
    
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    def set_date(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y
    
    def get_date(self):
        return f"{self.day}/{self.month}/{self.year}"
    
    def get_date_BC(self):
        return f"{self.day}/{self.month}/{self.year + 543}"
        
class Adress:
    def __init__(self, houseNo, street, district, city, country, postcode):
        self.houseNo = houseNo
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcode = postcode

    def set_adress(self, houseNo, street, district, city, country, postcode):
        self.houseNo = houseNo
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcode = postcode

    def get_adress(self):
        return f"{self.houseNo} {self.street} {self.district} {self.city} {self.country} {self.postcode}"
    
class Department:
    def __init__(self, description, manager, employeeList):
        self.description = description
        self.manager = manager
        self.employeeList = employeeList

    def add_employee(self, e):
        self.employeeList.append(e)
        e.department = self

    def delete_employee(self, e):
        self.employeeList.remove(e)
        e.department = None

    def setManager(self, e):
        if e in self.employeeList and e.is_permanent_employee():
            self.manager = e
        else:
            print("Error: Unable to set manager")

    def print_info(self):
        print(f"Department: {self.description}")
        if self.manager:
            print(f"Manager: {self.manager.name.get_Full_Name()}")
        else:
            print("Manager: None")
        print("Employee List:")
        for e in self.employeeList:
            print(f"\t{e.name.get_Full_Name()}")



class Person:
    def __init__(self, name, birthdate, adress):
        self.name = name
        self.birthdate = birthdate
        self.adress = adress

    def print_info(self):
        print(f"Name: {self.name.get_Full_Name()}")
        print(f"Birthdate: {self.birthdate.get_date()}")
        print(f"Adress: {self.adress.get_adress()}")
    
class Employee(Person):
    def __init__(self, name, birthdate, adress, startDate, department):
        super().__init__(name, birthdate, adress)
        self.startDate = startDate
        self.department = department

    def print_info(self):
        print(f"Name: {self.name.get_Full_Name()}")
        print(f"Birthdate: {self.birthdate.get_date()}")
        print(f"Adress: {self.adress.get_adress()}")
        print(f"Start Date: {self.startDate.get_date()}")
        print(f"Department: {self.department}")

class PermanentEmployee(Employee):
    def __init__(self, name, birthdate, adress, startDate, department, salary):
        super().__init__(name, birthdate, adress, startDate, department)
        self.salary = salary

    def is_permanent_employee(self):
        return True

    def print_info(self):
        print(f"Name: {self.name.get_Full_Name()}")
        print(f"Birthdate: {self.birthdate.get_date()}")
        print(f"Adress: {self.adress.get_adress()}")
        print(f"Start Date: {self.startDate.get_date()}")
        print(f"Department: {self.department.description}")
        print(f"Salary: {self.salary}")

class TemporaryEmployee(Employee):
    def __init__(self, name, birthdate, adress, startDate, department, wage):
        super().__init__(name, birthdate, adress, startDate, department)
        self.wage = wage

    def is_permanent_employee(self):
        return False

    def print_info(self):
        print(f"Name: {self.name.get_Full_Name()}")
        print(f"Birthdate: {self.birthdate.get_date()}")
        print(f"Adress: {self.adress.get_adress()}")
        print(f"Start Date: {self.startDate.get_date()}")
        print(f"Department: {self.department.description}")
        print(f"Wage: {self.wage}")


name = Name("Mr.", "Cusson", "L")
birthdate = Date(12, 2, 2005)
adress = Adress(54, "Ladkrabang", "Ladkrabang", "Bangkok", "Thailand", 10540)
startDate = Date(4, 1, 2020)
person = Person(name, birthdate, adress)
person.print_info()

print("--------------------------------------------------------------------------")

name2 = Name("Mr.", "Spoon", "E")
birthdate2 = Date(13, 2, 2005)
adress2 = Adress(55, "Ladkrabang", "Ladkrabang", "Bangkok", "Thailand", 10540)
startDate2 = Date(5, 1, 2020)
person2 = Person(name2, birthdate2, adress2)
person2.print_info()

print("--------------------------------------------------------------------------")

department = Department("KMITL", None, [])
employee = PermanentEmployee(name, birthdate, adress, startDate, department, 100000)
employee.print_info()
print("--------------------------------------------------------------------------")
employee2 = TemporaryEmployee(name2, birthdate2, adress2, startDate2, department, 20000)
employee2.print_info()

print("--------------------------------------------------------------------------")
department.add_employee(employee)
department.add_employee(employee2)
department.setManager(employee)
department.delete_employee(employee)
department.print_info()



        



