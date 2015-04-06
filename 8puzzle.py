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
				
					
