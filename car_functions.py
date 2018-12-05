import car as ss
import random


def gameplay():
	action = input ("whad do u want to do next (speed up or break): ")
	if action is 'speed up':
		ss.car.get_speed()
	elif action is 'break':
		ss.car.get_break()


def get_gas_calculattion():
	delta_gas = 10 / ss.car.speed
	ss.car.gas -= delta_gas
	if ss.car.gas <= 0:
		ss.car.state = 'dead'
	return ss.car.gas


def get_way_calculation():
	way = 1000
	step =  ss.car.speed * 1
	way -= step
	print (way)
	return way


def get_car_state():
	number = random.randint(0, 3)
	for state in ss.car.state:
		return ss.car.state[number]


def get_step():
	while ss.car.state:
		ss.car.turn_on()
		print (ss.car.gas)
		gameplay()
		get_gas_calculattion()
		get_way_calculation()
		get_car_state()
		ss.car.get_state_coef()
		print(ss.car.state, ss.car.gas)


get_step()

