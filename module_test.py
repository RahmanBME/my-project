import fibo
print("Hello, I am inside module_test")
n=fibo.find_fib(15)
print("15th fiboncci number is=",n)

import trial_module
print("Hlelo i am inside Module_test")
print(trial_module.__name__)


import sys
print(sys.path)
