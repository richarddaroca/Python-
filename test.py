class Coordinate(object):
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

	def __repr__(self):
		return 'Coordinate({},{})'.format(self.x, self.y) 

class Boundary(object):
	def __init__(self, x1 = 0, x2 = 0, y1 = 0, y2 = 0):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2

	def is_out_of_bounds(self, coordinate_tobe_tested):
		if 0 <= coordinate_tobe_tested.x and self.x2 - self.x1 >= coordinate_tobe_tested.x and 0 <= coordinate_tobe_tested.y and self.y2 - self.y1 >= coordinate_tobe_tested.y:
			return True
		else:
			return

class Person(object):
	def __init__(self, start , destination, obstacles, boundary):
		self.current_position = start
		self.destination = destination
		self.list_of_obstacles = obstacles
		self.boundary = boundary
		if self.boundary.is_out_of_bounds(self.current_position) != True:
			print 'Enter position is out of bounds'

		# print self.current_position		
		self.visual_aid()

	def move_up(self):
		self.current_position.y -= 1
		print self.current_position
		if self.check_for_obstacles() == True:
			print 'You have run into an obstacle'
			self.move_down()

		elif self.boundary.is_out_of_bounds(self.current_position) != True:
			self.move_down()

		else:
			self.are_we_there_yet()
			self.visual_aid()

	def move_down(self):
		self.current_position.y += 1
		print self.current_position
		if self.check_for_obstacles() == True:
			print 'You have run into an obstacle'
			self.move_up()

		elif self.boundary.is_out_of_bounds(self.current_position) != True:
			self.move_up()

		else:
			self.are_we_there_yet()
			self.visual_aid()

	def move_left(self):
		self.current_position.x -= 1
		print self.current_position
		if self.check_for_obstacles() == True:
			print 'You have run into an obstacle'
			self.move_right()
		
		elif self.boundary.is_out_of_bounds(self.current_position) != True:
			self.move_right()			
		
		else:
			self.are_we_there_yet()
			self.visual_aid()

	def move_right(self):
		self.current_position.x += 1
		print self.current_position
		if self.check_for_obstacles() == True:
			print 'You have run into an obstacle'
			self.move_left()

		elif self.boundary.is_out_of_bounds(self.current_position) != True:
			self.move_left()

		else:
			self.are_we_there_yet()
			self.visual_aid()

	def are_we_there_yet(self):
		if self.current_position.x == self.destination.x and self.current_position.y == self.destination.y:
			print "We have arrived"
		return

	def check_for_obstacles(self):
		for coordinate in self.list_of_obstacles:
			if self.current_position.x == coordinate.x and self.current_position.y == coordinate.y:
				return True

	def visual_aid(self):

		# Code for creating array
		self.playground_y = []
		self.playground_x = []

		for y in range(self.boundary.y1, self.boundary.y2 + 1 ):
			for x in range(self.boundary.x1, self.boundary.x2 + 1):
				self.playground_x.append('-')
			self.playground_y.append(self.playground_x)
			self.playground_x = []

		# print self.playground_y
		# self.playground_y[1][0] = 'p'
		# # print self.playground_y[1]
		# for x in self.playground_y:
		# 	print x
		# print self.playground_y
		for coordinate in self.list_of_obstacles:
			# print coordinate
			# print coordinate.x, coordinate.y
			self.playground_y[coordinate.y][coordinate.x] = 'O'


		self.playground_y[self.current_position.y][self.current_position.x] = 'P'
		self.playground_y[self.destination.y][self.destination.x] = 'D'

		# Code for displaying the array

		display = ''

		for y in self.playground_y:
			for x in y:
				display += x

			print display

			display = ''
		print '-------------------'


richard = Coordinate(2,2)
home = Coordinate(2,0)


list_of_obstacles = [Coordinate(0,1), Coordinate(0,0), Coordinate(1,1)]
border = Boundary(x1 = 2,  x2 = 6, y1 = 2, y2 = 6)

daroca = Person(richard, home, list_of_obstacles, border)
# print daroca.list_of_obstacles
# print daroca.current_position
# print daroca.destination

daroca.move_right()
daroca.move_right()
# print len(daroca.visual_aid.playground_y)
# daroca.move_right()
daroca.move_right()







# daroca.visual_aid()

# daroca.move_left()
# daroca.move_up()
# daroca.move_up()


# daroca.move_right()
# daroca.move_up()

# daroca.move_left()
# daroca.move_up()
# daroca.move_right()
# daroca.move_right()
# daroca.move_right()
# daroca.move_up()
# daroca.move_right()
# daroca.move_right()
# daroca.move_down()
# daroca.move_right()
# daroca.move_up()
# daroca.move_right()
# daroca.move_right()
# daroca.move_down()
# daroca.move_down()
# daroca.move_down()
# daroca.move_left()
# daroca.move_left()



# daroca.move_down()
# daroca.move_down()
# daroca.move_up()
# daroca.move_up()

# daroca.move_up()





