import matplotlib.pyplot as plt
import numpy as np
from xgboost.core import DMatrix
a=np.linspace(0,2*np.pi,50)
b=np.sin(a)
plt.plot(a,b)
plt.show()



