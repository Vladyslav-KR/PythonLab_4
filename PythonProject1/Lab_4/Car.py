class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0  # Початкова швидкість

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed


#  Створюємо об'єкт Car
car = Car("Toyota", "Camry", 2020)

#  Прискорення 5 разів
print("Прискорення:")
for i in range(5):
    car.accelerate()
    print(f"Швидкість після {i + 1} прискорення: {car.get_speed()} км/год")

#  Гальмування 5 разів
print("\nГальмування:")
for i in range(5):
    car.brake()
    print(f"Швидкість після {i + 1} гальмування: {car.get_speed()} км/год")
