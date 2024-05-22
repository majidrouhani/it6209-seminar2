import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from VanDerWaals import *

t_start = 223.15
t_end = 393.15
t_points = 940
t_range = np.linspace(t_start, t_end, t_points)

v_start = 0.00006
v_end = 0.001
v_steps = 0.000001
v_range = np.arange(v_start, v_end, v_steps)

vdw = VanDerWaals(1, 1, t_range, v_range)

p_values = vdw.calc_pressure_vdw()

plt.plot(t_range, p_values)
plt.show()