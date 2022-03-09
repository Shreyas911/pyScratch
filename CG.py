import numpy as np
import warnings

def linear_CG(action_of_matrix_on_vector, g, n, convergence_level):

	'''
	Generally used in solving H p = -g
	during Inexact Newton CG iterations

	action_of_matrix_on_vector - Function that returns action of nxn matrix H on any given n vector x
	g - Gradient, or more generally, negative of the RHS
	n - Should be dimensions of H and g
	convergence_level - 0 for linear, 1 for superlinear, 2 for quadratic
	'''

	# If g is a scalar getattr returns 1
	if getattr(g, '__len__', lambda:1)() != n:
		raise ValueError("Dimensions of g not equal to n.")

	if convergence_level == 0:
		eta = 0.5
	elif convergence_level == 1:
		eta = min(0.5, np.sqrt(np.linalg.norm(g)))
	elif convergence_level == 2:
		eta = min(0.5, np.linalg.norm(g))
	else:
		raise ValueError("Incorrect convergence level specified.")

	eps_TOL = eta*np.linalg.norm(g)


	p = np.zeros((n), dtype = float)
	Hp = action_of_matrix_on_vector(p)
	r = -g - Hp
	v = np.copy(r)

	i = 0
	while True:

		Hv = action_of_matrix_on_vector(v)

		alpha = np.dot(r,r) / np.dot(v,Hv)

		if np.dot(v,Hv) < 0:
			print(v, Hv)
			print("Hessian not positive definite, breaking now.")
			break

		p = p + alpha*v
		r_new = r - alpha*Hv

		if np.linalg.norm(r_new) <= eps_TOL:
			print("Tolerance achieved for linear CG.")
			break

		beta = np.dot(r_new,r_new) / np.dot(r,r)

		v = r_new + beta*v 

		i = i+1


		if i == n:
			warnings.warn("All conjugate directions explored.")
			break

		r = np.copy(r_new)

	return p

if __name__ == "__main__":

	A = np.diag(2.0**np.arange(1,6, dtype = float))

	# Define a function to compute action of A on vector x
	def action_of_A(x):
		return np.squeeze(np.matmul(A,x))

	# If you increase ||g||, we are far away from a minimum
	# So p won't be calculated super accurately
	p = linear_CG(action_of_A, 0.0001*np.ones((5)), 5, 1)


