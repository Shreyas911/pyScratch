import numpy as np

def Randomized_Range_Finder(action_of_matrix_on_vector, m, n, k, p):
	
	'''
	action_of_matrix_on_vector - Function that returns action of mxn matrix A on any given nx1 vector x
	m,n - Shape of A
	k - Desired rank of approximation
	p - Oversampling parameter, generally p = 5 or p = 10

	Returns 
	Q - An orthonormal matrix that has k <= l <= n columns, which captures the action of A
	'''

	l = k + p

	Omega = np.random.normal(0,1,size=(n,l))
	Y = np.zeros((m,l), dtype = float)
	
	for i in range(l):
		Y[:,i] = action_of_matrix_on_vector(Omega[:,i])

	Q, _ = np.linalg.qr(Y)
	
	return Q

def REVD(action_of_matrix_on_vector, n, k, p):

	'''
	action_of_matrix_on_vector - Function that returns action of nxn hermitian matrix A on any given nx1 vector x
	n - Shape of hermitian matrix A
	k - Desired rank of approximation
	p - Oversampling parameter, generally p = 5 or p = 10

	Returns
	U - Matrix containing eigenvectors of hermitian matrix A
	Ohm_vector - Array containing Eigenvalues of hermitian matrix A
	'''

	l = k + p

	Q = Randomized_Range_Finder(action_of_matrix_on_vector, n, n, k, p)
	
	AQ = np.zeros((n, l), dtype = float)

	for i in range(l):
		AQ[:,i] = action_of_matrix_on_vector(Q[:,i])
	
	T = np.matmul(Q.T, AQ)
	
	Ohm_vector, S = np.linalg.eig(T)
	
	U = np.matmul(Q,S)

	return U, Ohm_vector

if __name__ == "__main__":

	# Define a matrix with an exponential spectrum	
	A = np.diag(2.0**np.arange(1,41, dtype = float))

	# Define a function to compute action of A on vector x
	def action_of_A(x):
		return np.matmul(A,x)

	# REVD gives eigenmatrix and eigenvalues of A approximately
	U, Ohm_vector = REVD(action_of_A, 40, 10, 5)	

	# Compare approx eigenvalues to top 15 true values
	print(f'Actual - {np.sort(np.diag(A))[::-1][:15]}')
	print(f'Approx - {np.sort(Ohm_vector)[::-1]}')

	# Sort Ohm_vector and track sorted indices to similarly shuffle U to U_sorted
	indices = np.arange(0,15, dtype = int)
	indices_sorted = [x for _, x in sorted(zip(Ohm_vector, indices), key=lambda pair: pair[0])]
	
	# Shuffle U to U_sorted, you will see that bottom left to upper right diagonal contains 1.0 / -1.0 values
	U_sorted = U[:,indices_sorted]
	for i in range(40):
		print('\n')	
		for j in range(15):
			print(f'{U[i,j]:{"1.1e" if U[i,j] < 0 else " 1.1e"}} ', end='')
