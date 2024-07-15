class User:
    def __init__(self, first_name, last_name, age, email, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.hobby = hobby

    def describe_user(self):
        print("User information:")
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Age:", self.age)
        print("Email:", self.email)
        print("Hobby:", self.hobby)

    def greet_user(self):
        print(f"How are you today, {self.first_name}? How can I help you?\n")


o1 = User("Emma", "Jackson", 28, "ejackson@gmail.com", "baseball")
o2 = User("Allen", "Lu", 34, "alu@outlook.com", "swimming")
o3 = User("Kevin", "Garnett", 50, "kgarnett123@hotmail.com", "basketball")

o1.describe_user()
o1.greet_user()
o2.describe_user()
o2.greet_user()
o3.describe_user()
o3.greet_user()
