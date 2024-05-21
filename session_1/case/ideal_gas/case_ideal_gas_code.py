from messages import *
from constants_ideal_gas import *

def validate_input_type(calc_type, valid_options):
    """check that calc_type is valid.

    Args:
        calc_type (str): type of calculation

    Returns:
        BOOL: True if operation is valid
    """
    if calc_type not in valid_options:
        return False
    else:
        return True

def cal_amount_substance_in_mol(substance, amount):
    """calculate the amount of substance in mol.

    Args:
        substance (float): molar mass for the substance
        amount (float): amount of substance

    Returns:
        float: amount of substance in mol.
    """
    return amount/substance

def calc_volume(n, T_K, P):
    """calculating the volume for ideal gas.

    Args:
        n (float): amount of substance in mol.
        T_K (float): temperature in Kelvin
        P (float): Pressure.

    Returns:
        float: calculated volume.
    """
    return n*R_L_ATM_MOL_K*T_K/P

def calc_pressure(n, T_K, V):
    """calculating the pressure

    Args:
        n (float): amount of substance in mol.
        T_K (float): temperature in Kelvin
        V (float): volume

    Returns:
        float: calculated pressure
    """
    return n*R_L_ATM_MOL_K*T_K/V

def main():
    """ main program for calculating volume or pressure.
    """
    cont = True
    valid_options = ['V', 'P', 'Q']

    while (cont):

        # Input: type of calculation
        calc_type = input(
            MSG_IN_SELECT_CALC_TYPE.format(valid_options)).upper()

        input_is_valid = validate_input_type(calc_type, valid_options)

        # Input is not valid?
        if not input_is_valid:
            print(MSG_INVALID_OPTIONS.format(valid_options))
            continue

        # Quit?
        if calc_type == 'Q' and input_is_valid:
            cont = False
            continue

        # Calculate amount substance in mol, e.g. 35.8
        amount_substance_g = float(input(MSG_IN_AMOUNT_SUBSTANCE_MOL))
        n = cal_amount_substance_in_mol(MOLAR_MAS_O2, amount_substance_g)

        # Read temperature, e.g. 46
        temp_c = float(input(MSG_IN_TEMPERATURE_C))
        temp_K = temp_c + KELVIN_CONSTANT

        if calc_type == 'P':
            V = float(input(MSG_IN_VOLUME_L))  # e.g. 12.8
            P = calc_pressure(n, temp_K, V)
            print(MSG_OUT_PRESSURE_ATM.format(P))
        else:
            P = float(input(MSG_IN_PRESSURE_ATM))  # e.g. 2.29
            V = calc_volume(n, temp_K, P)
            print(MSG_OUT_VOLUME_L.format(V))


if __name__ == '__main__':
    main()