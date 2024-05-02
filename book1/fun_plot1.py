import numpy as np
import matplotlib.pyplot as plt

x= np.arange(0.0,20.0,0.1) # array x from 0 to 20 in increment of 0.1

def fun1(x):
    return 0.01*x**2+0.1*x

y= fun1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,y)
plt.show()