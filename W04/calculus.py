import math
value_1 = float(input('Enter with the first value: '))
value_2 = float(input('Enter with the second value: '))
sum = float(value_1+value_2)
diff = float(value_1 - value_2)
prod = float(value_1 * value_2)
div = float(value_1 / value_2)
int_div = float(value_1//value_2)
mod = float(value_1 % value_2)
exp = float (value_1 **value_2)
exp_2 = math.pow(value_1,value_2)

print (f'Sum = {sum}, Diff = {diff}, Product = {prod}, Division = {div}, Integer Division = {int_div}, Modulus = {mod}, Exponential = {exp}')