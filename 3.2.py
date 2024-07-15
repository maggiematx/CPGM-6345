class Student:
    # Class Variable, which is shared among all instances of 'Student' and its childclasses
    student_score = 95

    # constructor
    def __init__(self, name):
        # it increments the class variable 'student_score' by 10
        Student.student_score += 10
        # sets the instance's 'name'
        self.name = name

    # creates a method, which is inherited by all instances and subclasses of the 'Student' class
    def show(self):
        # prints a greeting that includes the name of the instance
        print("Hi, my name is " + self.name)


# Child class, which uses the methods and attributers of parent class 'Student'
class Ricestudent(Student):
    # no additional methods or attributes are added
    pass


# create an instance of 'Ricestudent' with the name "Peter"
o1 = Ricestudent("Peter")

# calls the 'show' method on o1
o1.show()

# prints the value of 'student_score'
print(o1.student_score)


"""The output should be:
Hi, my name is Peter
105

The child class Ricestudent inherits everything from the parent class Student. Therefore, it passes self.name as Peter.
The method o1.show() is defined inside the parent class Student, and it prints a statement with self.name, which is Peter.
The variable student_score is a class variable. When the instance o1 is created, it triggers the __init__ method, which increments student_score by 10 (from 95 to 105). Therefore, o1.student_score is 105."""
