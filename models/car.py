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


	def get_state(self):
		for x in random.randint(range(4)):
			return x

	def define_state(self, x):
		if x == 0:
			self.state = CarState.GOOD
		if x == 1:
			self.state = CarState.MEDIUM
		if x == 2:
			self.state = CarState.BAD
		else:
			self.state = CarState.DEAD

	@property
	def real_speed(self):
		return self.speed

	@real_speed.setter
	def real_speed(self, state):
		self.speed *= state.value

	@real_speed.getter
	def real_speed(self):
		return self.speed

	def change_stat(self, state: CarState):
		self.real_speed = state.value


class GasCar(Car):

	def __init__(self, gas=100):
		super(GasCar, self).__init__()
		self.gas = gas

	def turn_on(self):
		self.gas -= 5

	def get_speed(self):
		self.speed += 10

	def get_break(self):
		self.speed -= 7

	def is_alive(self):
		return self.state != 'dead' and self.gas != 0

car = GasCar()
car.state = ['good', 'medium', 'bad', 'dead']
bbb = GasCar()
bbb.hh = GOOD



