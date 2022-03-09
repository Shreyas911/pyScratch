import numpy as np

def backtrackingArmijoLineSearch(eval_obj_func, m, p, g, c1 = 1.e-4):

	alpha = 1.0

	while True:

		m_new = m + alpha * p

		descent = (eval_obj_func(m_new) - eval_obj_func(m)) / alpha*np.dot(p, g)
		
		if (descent > c1):
			break
		else:
			alpha = alpha/2.0
			continue


	return alpha

