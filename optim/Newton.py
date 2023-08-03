import CG
import line_search
import warnings
import numpy as np

def inexactNewtonCGiter(action_of_hessian_on_vector, 
						eval_obj_func, m, g, n, 
						convergence_level,
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

	p = CG.linear_CG(action_of_hessian_on_vector, m, g, n, convergence_level)
	alpha = line_search.backtrackingArmijoLineSearch(eval_obj_func, m, p, g, c1 = 1.e-4)

	m_new = m + alpha * p 

	return m_new

def L_BFGSiter(k, y_list, s_list, 
			eval_obj_func, get_gradient, 
			m_lbfgs, m, g, 
			c1 = 1.e-4, alpha_init = 1.0):

	'''
	Limitations - The curvature condition y^T.s > 0
				is not guaranteed with Armijo line search!

	K - iteration number starting from 0
	y_list - list of y_i = g_new - g_old
	s_list - list of s_i = m_new - m_old
	eval_obj_func - Evaluate objective function, takes in m as input
	get_gradient - Evaluate gradient at state m
	m_lbfgs - Number of vectors to store in memory
	m - state/control parameters
	g - Gradient
	c1 - Paramteter to quantify sufficient descent
	alpha_init - Initial guess for alpha, which decides the step length


	'''

	if k == 0:

		p = - 0.01*np.copy(g)

		alpha = line_search.backtrackingArmijoLineSearch(eval_obj_func, m, p, g, c1 = 1.e-4)
		m_new = m + alpha * p 

		s = alpha * p
		y = get_gradient(m_new) - get_gradient(m)
		y_list.append(y)
		s_list.append(s)

	elif k < m_lbfgs:

		q = - np.copy(g)

		alpha = np.zeros(k)

		for i in range(k-1, - 1, -1):

			alpha[i] = np.dot(s_list[i], q)/np.dot(y_list[i], s_list[i])
			q = q - alpha[i]*y_list[i]

		gamma = np.dot(y_list[-1], s_list[-1])/np.dot(y_list[-1], y_list[-1])

		p = gamma*q


		for i in range(k):
			beta = np.dot(y_list[i], p)/np.inner(y_list[i], s_list[i])
			p = p + (alpha[i] - beta)*s_list[i]

		alpha = line_search.backtrackingArmijoLineSearch(eval_obj_func, m, p, g, c1 = 1.e-4)

		m_new = m + alpha * p 

		s = alpha * p
		y = get_gradient(m_new) - get_gradient(m)

		if len(y_list) < m_lbfgs and len(s_list) < m_lbfgs and len(y_list) == len(s_list):
			y_list.append(y)
			s_list.append(s)
		elif len(y_list) == m_lbfgs and len(s_list) == m_lbfgs:
			y_list.pop(0)
			s_list.pop(0)
			y_list.append(y)
			s_list.append(s)

	else:
		q = - np.copy(g)

		alpha = np.zeros(k)

		for i in range(m_lbfgs-1, -1, -1):

			alpha[i] = np.dot(s_list[i], q)/np.dot(y_list[i], s_list[i])
			q = q - alpha[i]*y_list[i]

		gamma = np.dot(y_list[-1], s_list[-1])/np.dot(y_list[-1], y_list[-1])

		p = gamma*q

		for i in range(0, m_lbfgs):
			beta = np.dot(y_list[i], p)/np.inner(y_list[i], s_list[i])
			p = p + (alpha[i] - beta)*s_list[i]

		alpha = line_search.backtrackingArmijoLineSearch(eval_obj_func, m, p, g, c1 = 1.e-4)

		m_new = m + alpha * p 

		s = alpha * p
		y = get_gradient(m_new) - get_gradient(m)

		if len(y_list) < m_lbfgs and len(s_list) < m_lbfgs and len(y_list) == len(s_list):
			y_list.append(y)
			s_list.append(s)
		elif len(y_list) == m_lbfgs and len(s_list) == m_lbfgs:
			y_list.pop(0)
			s_list.pop(0)
			y_list.append(y)
			s_list.append(s)

	return m_new, s_list, y_list


if __name__ == '__main__':

	def eval_obj_func(m):
		return (m-100.0)**2

	def action_of_hessian_on_vector(m,x):
		return 2.0*x

	def get_gradient(m):
		return 2.*(m-100.0)


	#### COMMON CODE FOR BOTH
	m = 0.0
	m_old = 0.0
	MAX_ITERS = 100
	iters = 0

	#### TEST CODE FOR INEXACT NEWTON CG ####
	# while iters < MAX_ITERS:
	# 	g = get_gradient(m)

	# 	m = inexactNewtonCGiter(action_of_hessian_on_vector, eval_obj_func, m, g, 1, 1)
	# 	print(m)
	# 	iters = iters + 1

	# 	m_old = m

	#### TEST CODE FOR L-BFGS ####
	g = get_gradient(m)
	y_list = []
	s_list = []
	while iters < MAX_ITERS:
		g = get_gradient(m)

		m, s_list, y_list = L_BFGSiter(iters, y_list, s_list, eval_obj_func, get_gradient, 10, m, g, c1 = 1.e-4)
		iters = iters + 1

		m_old = m	
		print(m)

