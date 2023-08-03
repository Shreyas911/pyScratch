import numpy as np

def backtrackingArmijoLineSearch(eval_obj_func, m, p, g, c1 = 1.e-4, alpha_init = 1.0):

	'''
	Backtracking Armijo Line Search

	eval_obj_func - Evaluate objective function, takes in m as input
	m - Parameters
	p - Newton direction
	g - Gradient
	c1 - Paramteter to quantify sufficient descent
	alpha_init - Initial guess for alpha, which decides the step length
	Natural step length of Newton method is alpha = 1.0
	'''

	alpha = alpha_init

	while True:

		m_new = m + alpha * p

		descent = (eval_obj_func(m_new) - eval_obj_func(m)) / alpha*np.dot(p, g)

		if (descent > c1):
			break
		else:
			alpha = alpha/2.0
			continue


	return alpha

