import time


class Auto:
    def __init__(state, brand, age, weight = 1945):
        state.brand = brand
        state.age = age
        state.color = 'black'
        state.mark = 'CLS'
        state.weight = weight

    def move(state):
        print('move')
    
    def stop(state):
        print('stop')
    
    def birthday(state):
        state.age += 1

class Truck(Auto):
    def __init__(state, brand, age, mark, max_load):
        super().__init__(brand, age, mark)
        state.max_load = max_load

    def move(state):
        print('attention')
        super().move()

    def load(state):
        time.sleep(1)
        print('load')
        time.sleep(1)

class Car(Auto):
    def __init__(state, brand, age, mark, max_speed):
        super().__init__(brand, age, mark)
        state.max_speed = max_speed

    def move(state):
        super().move()
        print(f'max speed is {state.max_speed}')

new_car = Car('Mercedes-Benz', 3, 1945, 350)
new_car.move()
new_car.stop()
print(new_car.brand)
print(new_car.color)
print(new_car.age)
new_car.birthday
