import os

# change working folder
path = os.getcwd() + "/seminar_2/session_1/src/case/ideal_gas/"
os.chdir(path)


# import functions
from case_ideal_gas_code import cal_amount_substance_in_mol, calc_pressure, calc_volume

# get functions docstrings
print (cal_amount_substance_in_mol.__doc__)
print (calc_pressure.__doc__)
print (calc_volume.__doc__)