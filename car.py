

class Car(object):

	def __init__(self, speed=0, state='good', alive=True):
		self.speed = speed
		self.state = ['good', 'medium', 'bad', 'dead']
		self.alive = alive


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
			speed = speed

		elif self.satate is medium:
			self.speed *= 0.85

		elif self.state is bad:
			self.speed *= 0.6

		else: 
			self.speed = 0

car = GasCar(0, 'good', 'alive')
yg