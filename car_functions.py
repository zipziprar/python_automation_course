import car as ss
import random


def get_car_state():
	number = random.randint(0, 3)
	for state in ss.car.state:
		return ss.car.state[number]


print(get_car_state())

print (ss.car.state)