#assignment
'''
University System Display information of
Classes: Person (parent), and subclasses Student , lecturer, Staff.
'''
class Person:
    def __init__(self, name, gender, age, nationality):
        self.name = name
        self.gender = gender
        self.age = age
        self.nationality = nationality
        
    def present(self):
        print(f"name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nNationality: {self.nationality}")
        
class Student(Person):
    def __init__(self, name, gender, age, nationality):
        super().__init__(name, gender, age, nationality)
        self.regitarionNumber = input(f"Dear {self.name} Please Enter your registration number: \n")
        self.course = input("Enter your course: \n")
        self.yearOfStudy = input("Enter your year of study: \n")
    #overiding the present method
    def present(self):
        print()
        print("Student Information:")
        super().present()
        print("Registration Number: ", self.regitarionNumber)
        print("Course: ", self.course)
        print("Year of Study: ", self.yearOfStudy)
        print()

class Lecturer(Person):
   def __init__(self, name, gender, age, nationality):
       super().__init__(name, gender, age, nationality)
       self.employeeId = input(f"Dear {self.name} PleaseEnter your employee ID: \n")
       self.department = input("Enter the department within which you work: \n")
       
   def present(self):
       print()
       print("Lecturer Information:")
       super().present()
       print("Employee ID: ", self.employeeId)
       print("Department: ", self.department)
       print()

class Staff(Person):
    def __init__(self, name, gender, age, nationality):
        super().__init__(name, gender, age, nationality)
        self.staffId = input(f"Dear {self.name} Please Enter your staff ID: \n")
        self.role = input("Enter your role: \n")
        
    def present(self):
        print()
        print("Staff Information:")
        super().present()
        print("Staff ID: ", self.staffId)
        print("Role: ", self.role)
        
student = Student("Ayan Mustafa", "Female", 21, "Somali")
student.present()
lecturer = Lecturer("Dr. Ahmed Ali", "Male", 45, "Arab")
lecturer.present()
staff = Staff("Fatima Hassan", "Female", 30, "kenyan")
staff.present()
            