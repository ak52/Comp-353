goal_state = [[1,2,3],[4,5,6],[7,8,0]]
initial_state = [[1,0,3],[4,2,5],[7,8,6]]

def convert_to_1D(matrix_2D):
	matrix_1D = list()
	for row in range(len(matrix_2D)):
		for col in range(len(matrix_2D)):
			matrix_1D.append(matrix_2D[row][col])
	return matrix_1D

print convert_to_1D(goal_state)
print convert_to_1D(initial_state)

def inversion(matrix_2D):
	m_1D = convert_to_1D(matrix_2D)
	inv = 0
	for i in range(len(m_1D)):
		if(m_1D.index(i) < i and m_1D.index(i) != 0):
			inv += 1
	return inv

print inversion(initial_state)		
			
def find_N(matrix_2D):
	m_1D = convert_to_1D(matrix_2D)
	inversion = 0
	for index in range(len(m_1D)):
		temp = m_1D[index]
		if temp == 0 or temp == 1:
			continue
		for elem in m_1D[index:]:
			if elem == 0:
				continue
			if (temp > elem):
				inversion += 1
	return inversion

print find_N(initial_state)
				
# is_valid 2-dimensional arrays-of-numbers -> boolean

def is_valid(matrix_2D):

	""" checks whether the given matrix is valid or not """
	sum_of_numbers = 0
	sum_of_squares = 0
	m_1D = convert_to_1D(matrix_2D)
	for index in range(len(m_1D)):
		sum_of_numbers += m_1D[index]
		sum_of_squares += pow(m_1D[index],2)
	if sum_of_numbers == 36 and sum_of_squares == 204:
		return True
	else:
		return False

# is_solvable 2-dimesional arrays-of-numbers -> boolean

def is_solvable(matrix_2D):

	""" checks whether the given matrix is solvable or not """
	goal = find_N(goal_state)
	initial = find_N(matrix)
	if (goal % 2) == 0 and (initial % 2) == 0:
		return True
	elif (goal % 2) == 1 and (initial % 2) == 1:
		return True
	else:
		return False
				
					
