class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


car1 = Car("Ford", "Mustang")

car1.move()
