import numpy as np

class VanDerWaals:
    """
    Class to calculate the pressure of a gas using the Van der Waals equation of state.
    
    Attributes
    ----------
    pc : float
        The critical pressure of the gas in bar, converted to Pa.
    tc : float
        The critical temperature of the gas in Kelvin.
    t_values : numpy.ndarray
        An array of temperature values in Kelvin.
    v_values : numpy.ndarray
        An array of volume values in m^3.

    Methods
    -------
    calc_pressure_vdw()
        Calculates the pressure of the gas using the Van der Waals equation of state.
    """    
    
    # Gas constant in l.atm/(mol.K)
    R = 8.314462618
    
    ATTRACTION_FACTOR = 27
    VOLUME_FACTOR = 64
    CRITICAL_FACTOR = 8
    PRESSURE_CONVERSION_FACTOR = 100000
        
    def __init__(self, pc, tc, t_values, v_values):
        """
        Constructs all the necessary attributes for the VanDerWaals object.

        Parameters
        ----------
        pc : float
            The critical pressure of the gas in bar.
        tc : float
            The critical temperature of the gas in Kelvin.
        t_values : numpy.ndarray
            An array of temperature values in Kelvin.
        v_values : numpy.ndarray
            An array of volume values in m^3.
        """
        
        # Checking if the inputs are valid
        if not isinstance(pc, (int, float)) or pc <= 0: 
            raise ValueError("Pc must be a positive number")        
        if not isinstance(tc, (int, float)) or tc <= 0: 
            raise ValueError("Tc must be a positive number")
        if not isinstance(t_values, np.ndarray) or t_values.size == 0: 
            raise ValueError("Temperature values must be a non-empty numpy array")
        if not isinstance(v_values, np.ndarray) or v_values.size == 0: 
            raise ValueError("Volume values must be a non-empty numpy array")
        if not np.all(v_values > 0): 
            raise ValueError("Volume values should be positive")

        # Saving the inputs as object attributes
        self.pc = pc * VanDerWaals.PRESSURE_CONVERSION_FACTOR  # Converting pressure units, Pa
        self.tc = tc
        self.t_values = t_values
        self.v_values = v_values
        
        self.a = (VanDerWaals.ATTRACTION_FACTOR * VanDerWaals.R**2 * self.tc**2) / (VanDerWaals.VOLUME_FACTOR * self.pc)
        self.b = (VanDerWaals.R * self.tc) / (VanDerWaals.CRITICAL_FACTOR * self.pc)
        

    def calc_pressure(self):
        """
        Calculates the pressure of the gas using the Van der Waals equation of state.

        The Van der Waals equation of state is a mathematical model that describes the behavior of real gases. 
        It takes into account the finite size of molecules and the intermolecular attractions.

        Returns
        -------
        numpy.ndarray
            An array of pressure values in Pa.
        """
                
        if np.any(self.v_values == self.b):
            raise ValueError("Volume values should not be equal to b")
    
        p = ((VanDerWaals.R * self.t_values) / (self.v_values - self.b)) - (self.a / self.v_values**2)
        return p