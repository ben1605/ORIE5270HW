from scipy.optimize import minimize, rosen, rosen_der
import numpy as np

for i in range(200):
    x0 = np.random.uniform(-100,100,3)
    res = minimize(rosen, x0,method='BFGS',jac=rosen_der)
    print(res.x)