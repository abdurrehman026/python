class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.gender = None
        self.location = None

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def set_gender(self, gender):
        self.gender = gender

    def set_location(self, location):
        self.location = location


name = input("What is your name? ")
user = User(name)
user.set_age(input("What is your age? "))
user.set_gender(input("What is your gender? "))
user.set_location(input("Where do you live? "))
print("Name:", user.get_name())
print("Age:", user.age)
print("Gender:", user.gender)
print("Location:", user.location)
