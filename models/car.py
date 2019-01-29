from enum import Enum
import random
import json


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
#			return (self.alive = False)

	@state.getter
	def state (self, state):
		return self.state


	def change_stat(self, state: CarState):
		self.real_speed = state.value


class GasCar(Car):

	def __init__(self, model, gas, max_speed):
		super(GasCar, self).__init__()
		self.model = model
		self.gas = gas
		self.max_speed = max_speed

	def turn_on(self):
		self.gas -= 5

	def get_speed(self):
		self.speed =  self. speed * state.value + 10

	def get_break(self):
		self.speed -= 7

	def is_alive(self):
		return self.state != 'dead' and self.gas != 0



class CarsFactory(object):
    @classmethod
    def get_car_by_model(cls, model, source):
        cars_from_json = get_list_of_cars(source)
        list_of_cars = cars_from_json.get("cars") 
        if not list_of_cars:
            return None
        for car in list_of_cars:
            if model in car["model"]:
                return GasCar(car["model"], car["gas"], car["max_speed"])



def get_list_of_cars(filename):
    with open(filename, 'r') as f:
        cars_obj = json.load(f)
    return cars_obj


