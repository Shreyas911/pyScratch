import CG
import line_search
import warnings
import numpy as np

def inexactNewtonCGiter(action_of_hessian_on_vector, eval_obj_func, m, g, n, convergence_level,
						c1 = 1.e-4, alpha_init = 1.0):

	'''
	action_of_matrix_on_vector - Function that returns action of nxn matrix H on any given n vector x
	eval_obj_func - Evaluate objective function, takes in m as input
	m - Parameters
	p - Newton direction
	g - Gradient
	convergence_level - 0 for linear, 1 for superlinear, 2 for quadratic
	c1 - Paramteter to quantify sufficient descent
	alpha_init - Initial guess for alpha, which decides the step length
	'''

	p = CG.linear_CG(action_of_hessian_on_vector, g, n, convergence_level)
	alpha = line_search.backtrackingArmijoLineSearch(eval_obj_func, m, p, g, c1 = 1.e-4)

	m_new = m + alpha * p 

	return m_new

if __name__ == '__main__':

	def eval_obj_func(m):
		return (m-100.0)**2

	def action_of_hessian_on_vector(m):
		return 2.0*m 

	def get_gradient(m):
		return 2.*(m-100)

	m = 0.0
	m_old = 0.0
	MAX_ITERS = 10
	iters = 0
	while iters < MAX_ITERS:

		g = get_gradient(m)

		m = inexactNewtonCGiter(action_of_hessian_on_vector, eval_obj_func, m, g, 1, 1)
		print(m)
		iters = iters + 1

		if(m-m_old < 1.0):
			break

		m_old = m