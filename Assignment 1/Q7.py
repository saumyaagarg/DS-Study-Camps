''' Simulate a Zoo Management System
Requirements:
Implement classes for Animal, Mammal, Bird, Reptile, ZooKeeper, and Zoo.
Animal should be a base class with attributes like name, species, age, and methods like eat and sleep.
Mammal, Bird, and Reptile should inherit from Animal and add specific attributes/methods.
ZooKeeper should have attributes like name, employee_id, and methods to take care of animals.
Zoo should manage a collection of animals and provide methods to add/remove animals, assign zookeepers, and generate reports on animals. '''

class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def __str__(self):
        return f"Name: {self.name}, Species: {self.species}, Age: {self.age} years"


class Mammal(Animal):
    def __init__(self, name, species, age, fur_colour):
        super().__init__(name, species, age)
        self.fur_colour = fur_colour

    def nurse(self):
        print(f"{self.name} is nursing its young.")

    def __str__(self):
        return f"{super().__str__()}, Fur Colour: {self.fur_colour}"


class Bird(Animal):
    def __init__(self, name, species, age, wing_span):
        super().__init__(name, species, age)
        self.wing_span = wing_span

    def fly(self):
        print(f"{self.name} is flying.")

    def __str__(self):
        return f"{super().__str__()}, Wing Span: {self.wing_span} meters"


class Reptile(Animal):
    def __init__(self, name, species, age, is_venomous):
        super().__init__(name, species, age)
        self.is_venomous = is_venomous

    def shed_skin(self):
        print(f"{self.name} is shedding its skin.")

    def __str__(self):
        venomous_text = "Venomous" if self.is_venomous else "Non-venomous"
        return f"{super().__str__()}, {venomous_text}"


class ZooKeeper:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def take_care(self, animal):
        print(f"{self.name} is taking care of {animal.name} the {animal.species}.")

    def __str__(self):
        return f"ZooKeeper: {self.name}, Employee ID: {self.employee_id}"


class Zoo:
    def __init__(self):
        self.animals = []
        self.zookeepers = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Added {animal.name} the {animal.species} to the zoo.")

    def remove_animal(self, animal_name):
        for animal in self.animals:
            if animal.name == animal_name:
                self.animals.remove(animal)
                print(f"Removed {animal.name} the {animal.species} from the zoo.")
                return
        print(f"Animal named {animal_name} not found in the zoo.")

    def assign_zookeeper(self, zookeeper):
        self.zookeepers.append(zookeeper)
        print(f"Assigned {zookeeper.name} as a zookeeper.")

    def generate_report(self):
        print("Zoo Report:")
        print("Animals in the Zoo:")
        if not self.animals:
            print("No animals in the zoo.")
        else:
            for animal in self.animals:
                print(animal)
        print("\nZookeepers in the Zoo:")
        if not self.zookeepers:
            print("No zookeepers assigned.")
        else:
            for zookeeper in self.zookeepers:
                print(zookeeper)

    def __str__(self):
        return f"Zoo has {len(self.animals)} animals and {len(self.zookeepers)} zookeepers."


# Example usage
zoo = Zoo()

# Adding animals
lion = Mammal("Saja", "Lion", 5, "Golden")
parrot = Bird("Aengmusae", "Parrot", 2, 0.5)
snake = Reptile("Baem", "Snake", 3, True)

zoo.add_animal(lion)
zoo.add_animal(parrot)
zoo.add_animal(snake)
print()

# Assigning zookeepers
zookeeper1 = ZooKeeper("Ryan", "ZK1")
zookeeper2 = ZooKeeper("Blake", "ZK2")

zoo.assign_zookeeper(zookeeper1)
zoo.assign_zookeeper(zookeeper2)
print()

# Zookeepers taking care of animals
zookeeper1.take_care(lion)
zookeeper2.take_care(parrot)
print()

# Generating zoo report
zoo.generate_report()
print()

# Removing an animal
zoo.remove_animal("Aengmusae")
print()

# Generating report after removal
zoo.generate_report()