class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0

    def get_speed(self):
        return self.speed

# Створення об'єкта класу Car
my_car = Car("Toyota", "Camry", 2018)

# Виклик методу accelerate п'ять разів і друкування поточної швидкості
print("Accelerating...")
for _ in range(5):
    my_car.accelerate()
    print(f"Current speed: {my_car.get_speed()} km/h")

# Виклик методу brake п'ять разів і друкування поточної швидкості
print("\nBraking...")
for _ in range(5):
    my_car.brake()
    print(f"Current speed: {my_car.get_speed()} km/h")
