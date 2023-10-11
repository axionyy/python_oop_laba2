class Car:
    color = None
    fuel = None
    mark = None
    motor = None

    def go(self):
        pass

    def turn(self):
        pass

    def stop(self):
        pass

    def output(self, car):
        print(f'color:{car.color}'
              f'\nfuel:{car.fuel}'
              f'\nmark:{car.mark}'
              f'\nmotor:{car.motor}')

myCar = Car()

myCar.color = 'black'
myCar.fuel = 50
myCar.mark = 'Honda'
myCar.motor = 1.8

myCar.output(myCar)