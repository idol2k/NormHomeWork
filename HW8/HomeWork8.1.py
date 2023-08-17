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
        
new_car = Auto('Mercedes-Benz', 3, 1945)
new_car.birthday()
new_car.move()
new_car.stop()
print(new_car.brand)
print(new_car.color)
print(new_car.age)