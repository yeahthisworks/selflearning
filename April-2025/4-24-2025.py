# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

my_dog = Dog("Buddy")
print(my_dog.speak())  # Calls the speak method of the Dog class