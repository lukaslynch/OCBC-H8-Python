import sys 
import person
# import person as my_person
# from person import name, display, devices
from person import name as p_name, display as p_display, devices as p_devices
from person import *
import car
import importlib

# print(person.name)
# print("------------")
# print(person.devices)
# print("------------")
# person.display('Hello Guys!')

#print(sys.path)

# print(person)
# print(car)
# print(p_name)
# p_display('Halo')
# print(p_devices)
# print(dir())
# print(dir(person))
# print(sys.__name__)

# # print(re.__file__)

# import person
# dir(person)

# from person import name, devices
# dir(name)
print(car)
print('brands: ',car.brands)

# importlib.reload(car)