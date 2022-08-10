a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():

        a = "I am local variable!"
        print(a)


def enclosing_funcion_5_4_1():
    a = "I am variable from enclosed function!"

    def inner_function():

        a = "I am local variable!"
        print(a)

    return inner_function


def enclosing_funcion_5_4_2():
    a = "I am variable from enclosed function!"

    def inner_function():
        global a
        #a = "I am local variable!"
        print(a)

    return inner_function


def enclosing_funcion_5_4_3():
    a = "I am variable from enclosed function!"

    def inner_function():
        nonlocal a
        #a = "I am local variable!"
        print(a)

    return inner_function
