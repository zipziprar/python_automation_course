from enum import Enum
import random


class CarState(Enum):
	GOOD = 1.0,
	MEDIUM = 0.85,
	BAD = 0.6,
	DEAD = 0


class Car(object):

	def __init__(self):
		self.state = None
		self.speed = 0
		self.alive = True


	state = property()

	def define_state(self, x):
		''''''

	@property
	def state (self, state_number):
		if state_number == 0:
			self.state = CarState.GOOD
		if state_number == 1:
			self.state = CarState.MEDIUM
		if state_number == 2:
			self.state = CarState.BAD
		else:
			self.state = CarState.DEAD
		return self.speed

	@state.getter
	def state (self, state):
		return self.state


	def change_stat(self, state: CarState):
		self.real_speed = state.value


class GasCar(Car):

	def __init__(self, gas=100):
		super(GasCar, self).__init__()
		self.gas = gas

	def turn_on(self):
		self.gas -= 5

	def get_speed(self):
		self.speed * state.value += 10

	def get_break(self):
		self.speed -= 7

	def is_alive(self):
		return self.state != 'dead' and self.gas != 0


with open ('cars.json', 'r') as obj:
	data = obj.read()

json_cars = json.loads(data)
cars = json_cars["cars"]
print(json_cars)

gas_car_object = GasCar(cars[0]["model"], cars[0]["gas"])

print(gas_car_object)




