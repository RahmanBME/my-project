'''A module is simply a Python file (.py) that contains functions, variables, or classes that you can use in other Python programs.
A package is a collection of modules, stored in a folder, with a special __init__.py file (even if it's empty).
'''

import builtins
print(dir(builtins))

import math
print(math.pi)

#now we will try to know the today's date
import datetime
today=datetime.date.today()
print(today)

#daate with time
today=datetime.datetime.today()
print(today)


