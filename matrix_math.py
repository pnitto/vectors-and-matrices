from functools import reduce
from math import sqrt


class ShapeException(Exception):

    pass

def shape(m):
    if type(m[0]) == type(list()):
        return (len(m),len(m[0]))
    return (len(m), )

def check_shapes(x,y):
    if shape(x) != shape(y):
        raise ShapeException


def dot(x, y):
    check_shapes(x,y)
    dot_list = []
    for index, value in enumerate(x):
        dot_list.append(x[index] * y[index])
    return sum(dot_list)

def magnitude(x):
    return sqrt(dot(x,x))


def vector_add(x, y):
    check_shapes(x,y)
    add_list = []
    for index, value in enumerate(x):
        add_list.append(y[index] + value)
    #print(add_list)
    return add_list


def vector_sub(x, y):
    check_shapes(x,y)
    sub_list = []
    for index, value in enumerate(y):
        sub_list.append(x[index] - value)
    #print(sub_list)
    return sub_list


def vector_sum(*args):
    #print(reduce(vector_add,args))
    return reduce(vector_add,args)


def vector_multiply(x,number):
    multiply_list = []
    for index,value in enumerate(x):
        multiply_list.append(x[index] * number)
    return multiply_list


def vector_mean(*args):
    return vector_multiply(vector_sum(*args), (1/len(args)))


def matrix_row(x, y):
    return x[y]


def matrix_col():
    pass


def matrix_scalar_multiply():
    pass


def matrix_vector_multiply():
    pass


def matrix_matrix_multiply():
    pass


