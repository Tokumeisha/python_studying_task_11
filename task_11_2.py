class Car:
    __brand = 'Schubert'
    __model = 'Six'
    __year = 1933
    __speed = 0
    __speed_vector = 1
    def increase_speed(self):
        car._Car__speed = car._Car__speed + (car._Car__speed_vector * 5)
    def decrease_speed(self):
        car._Car__speed = car._Car__speed - (car._Car__speed_vector * 5)
    def stop(self):
        car.speed = 0
    def show_speed(self):
        print('Car speed is', car._Car__speed)
    def reverse(self):
        car._Car__speed_vector = -car._Car__speed_vector
        car._Car__speed = car._Car__speed * car._Car__speed_vector
        
car = Car()
