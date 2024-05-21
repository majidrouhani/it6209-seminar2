import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from VanDerWaals import *

t_range = np.arange(223.15, 393.15, 10)
v_range = np.arange(0.00006, 0.001, 0.000001)
p_vdw = VanDerWaals(1, 1, t_range, v_range, 0.0821, 273.15)

p_calc = p_vdw.generate_pressure_grid()

print(p_calc)