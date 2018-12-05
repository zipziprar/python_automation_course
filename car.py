import random

class Car(object):

	def __init__(self, alive, speed=0, state='good'):
		self.speed = speed
		self.state = state
		self.alive = True


class GasCar(Car):

	def __init__(self, speed, state, alive, gas=100):
		super().__init__(speed, state, alive)
		self.gas = gas

	def turn_on(self):
		self.gas -= 5

	def get_speed(self):
		self.speed += 10

	def get_break(self):
		self.speed -= 7

	def get_state_coef(self):
		if self.state is good:
			self.speed = speed

		elif self.satate is medium:
			self.speed *= 0.85

		elif self.state is bad:
			self.speed *= 0.6

		elif self.state is dead: 
			self.speed = 0

	def is_alive(self):
		return self.state != 'dead' and self.gas != 0

car = GasCar(0, 'state', 'alive')
car.state = ['good', 'medium', 'bad', 'dead']

