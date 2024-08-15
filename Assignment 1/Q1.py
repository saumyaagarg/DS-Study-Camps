# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person’s age. 

from datetime import datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, "%d-%m-%Y")
    
    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.dob.year

        # Checking if the birthday has occurred yet this year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
        return age

    def __str__(self):
        return f"Name: {self.name}, Country: {self.country}, Age: {self.calculate_age()}"

# Example usage
person = Person("Yoon Jeonghan", "South Korea", "04-10-1995")
print(person)
