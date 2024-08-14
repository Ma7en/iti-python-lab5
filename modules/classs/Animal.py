class Animal:
    def __init__(
        self,
        name,
        age,
    ):
        self.name = name
        self.age = age

    def eat(self):
        print(f"({self.name}) is eating.")

    def drink(self):
        print(f"({self.name}) is drinking.")


class Cat(Animal):
    def __init__(
        self,
        name,
        age,
    ):
        super().__init__(name, age)

    def meow(self):
        print(f"({self.name}) is meowing.")

    def eat(self):
        print(f"({self.name}) is eating its favorite food.")
