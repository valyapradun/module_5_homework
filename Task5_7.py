"""
------------------------------
Run the module modules/mod_a.py. Check its result. Explain why does this happen.
------------------------------
>>> 1000
It's because of the import order: mod_b then mod_c
In mod_b global x is changed to 1000 and when import from mod_c happens, x is already = 1000


------------------------------
Try to change x to a list [1,2,3]. Explain the result.
------------------------------
>>> 1000
If we change x in mod_c. Same as previous explanation
or
>>> [1, 2, 3]
If we change x in mod_b. Because we change value of global x there


------------------------------
Try to change import to 'from x import *' where x - module names. Explain the result.
------------------------------
>>> 6
If we change 'from mod_c import *' in mod_b. And remove 'mod_c.' in mod_c.x = 1000
Because in this case all global variable have the same name, the result will be dependent of the import order.
The last one is mod_c, in this module x = 6

>>> 1000
If we change 'from mod_b import *' in mod_c.
The same explanation as point 1
"""