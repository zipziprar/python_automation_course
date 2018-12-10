from enum import Enum
import random


class CarState(Enum):
	GOOD = 1.0,
	MEDIUM = 0.85,
	BAD = 0.6,
	DEAD = 0


class Car(object):

	def __init__(self):
		self.speed = 0
		self.alive = True

	def move(self):
		"""  """

	@property
	def real_speed(self):
		return self.speed

	@real_speed.setter
	def real_speed(self, state):
		self.speed *= state.value

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



