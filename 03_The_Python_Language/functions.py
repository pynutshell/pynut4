from math import sin, cos, tan, asin, acos, atan, log, exp

def add_inverses(i_dict):
    for f in list(i_dict):  #  iterates over keys while mutating i_dict
        i_dict[i_dict[f]] = f

math_map = {sin: asin, cos: acos, tan: atan, log: exp}
add_inverses(math_map)


for k, v in math_map.items():
    print(k.__name__, v.__name__)



def twice(x):
    return x*2

print(twice(100))
print(twice('ciao'))
