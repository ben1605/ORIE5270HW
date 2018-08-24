from scipy.optimize import minimize
import numpy as np

def rosen(x):
    """
    This function defines rosenbrock function.
    :param x: this is a 3-dimensional list representing x.
    :return: the value of rosenbrock function
    """
    return 100*(x[1]-x[0]**2)**2+(1-x[0])**2+100*(x[2]-x[1]**2)**2+(1-x[1])**2

def deriv(x):
    """
    This function defines the first derivative of rosenbrock function.
    :param x: this is a 3-dimensional list representing x.
    :return: the 3-dimensional vector of gradient.
    """
    return np.array([400*x[0]**3-400*x[1]*x[0]-2+2*x[0], 
		     400*x[1]**3-400*x[2]*x[1]-200*x[0]**2-2+202*x[1],
                     200*x[2]-200*x[1]**2])

if __name__ == "__main__":
    for i in range(20):
        x0 = np.random.uniform(-100,100,3)
        temp = minimize(rosen, x0,method='BFGS',jac=deriv)
        print("Optimal point:",temp.x," Minimum of objective function:", temp.fun)

