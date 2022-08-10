"""
Look through file modules/legb.py.
1) Find a way to call `inner_function` without moving it from inside of `enclosed_function`.
2) Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.
3) Modify ONE LINE in `inner_function` to make it print variable 'a' form enclosing function.
"""

import modules.legb as legb

if __name__ == '__main__':
    legb.enclosing_funcion_5_4_1()()  # I am local variable!
    legb.enclosing_funcion_5_4_2()()  # I am global variable!
    legb.enclosing_funcion_5_4_3()()  # I am variable from enclosed function!
