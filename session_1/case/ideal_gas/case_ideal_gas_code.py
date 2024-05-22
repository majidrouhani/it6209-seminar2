from messages import *
from constants_ideal_gas import *


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
        # Get user input for calculation type and convert to uppercase
        calc_type = input(
            MSG_IN_SELECT_CALC_TYPE.format(valid_options)).upper()

        # Check if user input is valid
        input_is_valid = calc_type in valid_options

        # If input is not valid, print error message and continue to next iteration
        if not input_is_valid:
            print(MSG_INVALID_OPTIONS.format(valid_options))
            continue

        # If user chose to quit, set continue flag to False and continue to next iteration
        if calc_type == 'Q':
            cont = False
            continue

        # Get user input for amount of substance in grams, e.g. 35.8
        try:
            amount_substance_g = float(input(MSG_IN_AMOUNT_SUBSTANCE_MOL))
        except ValueError:
            # If input is not a number, print error message and continue to next iteration
            print(MSG_INVALID_VALUE)
            continue
        
        # Calculate amount of substance in moles
        n = cal_amount_substance_in_mol(MOLAR_MAS_O2, amount_substance_g)

        # Get user input for temperature in degreee, e.g. 46
        try:
            temp_c = float(input(MSG_IN_TEMPERATURE_C))
        except ValueError:
            print(MSG_INVALID_VALUE)
            continue

        # Check that temperature is above absolute zero
        if temp_c < -KELVIN_CONSTANT: 
            print(MSG_INVALID_TEMPERATURE_VALUE.format(-KELVIN_CONSTANT))
            continue

        temp_K = temp_c + KELVIN_CONSTANT

        # if user chose to calculate pressure
        if calc_type == 'P':
            try:
                V = float(input(MSG_IN_VOLUME_L))  # e.g. 12.8
            except ValueError:
                print(MSG_INVALID_VALUE)
                continue

            if V <= 0:  # Check that volume is positive
                print(MSG_INVALID_VOLUME)
                continue

            P = calc_pressure(n, temp_K, V)
            print(MSG_OUT_PRESSURE_ATM.format(P))
        
        # if user chose to calculate volume
        else:
            try:
                P = float(input(MSG_IN_PRESSURE_ATM))  # e.g. 2.29
            except ValueError:
                print(MSG_INVALID_VALUE)
                continue

            if P <= 0:  # Check that pressure is positive
                print(MSG_INVALID_PRESSURE)
                continue

            V = calc_volume(n, temp_K, P)


if __name__ == '__main__':
    main()
