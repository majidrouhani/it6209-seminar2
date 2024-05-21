import numpy as np

class VanDerWaals:
    def __init__(self, Pc, Tc, T_range, V_range, R, KC):
        self.Pc = Pc * 100000  # Converting pressure units, Pa
        self.R = R  # Universal gas constant, (m3.Pa)/(mol.K)
        self.KC = KC
        self.Tc = Tc
        self.T_range = T_range
        self.V_range = V_range

    def calc_pressure_vdw(self, T, V):
        a = (27 * self.R**2 * self.Tc**2) / (64 * self.Pc)
        b = (self.R * self.Tc) / (8 * self.Pc)
        P = ((self.R * T) / (V - b)) - (a / V**2)
        return P

    def generate_pressure_grid(self):
        T_values, V_values = np.meshgrid(self.T_range, self.V_range)
        P_values = self.calc_pressure_vdw(T_values, V_values)
        return P_values