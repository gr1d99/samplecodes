# =========================================================================
def some_notes():
    notes = """
    A function is asequence of statements which perfom some kind of a task.
    We mostly use functions to eliminate code duplication.

    Python has some inbuilt functions, some of them are
        : ``print``
        : ``len``
    """

    print(notes)

# ==========================================================================


def fun1():
    """
    Because defining a function does not cause it to execute,
    we can use an identifier inside a function even if it hasn't been defined yet
     - as long as it becomes defined by the time we run the function.

    : fun()1 calls fun2()
    """
    fun2()


def fun2():
    print("hey i'm fun2() and I was just called by another function up there.")

# try moving fun2() above fun1() and see if the code will run

# ===========================================================

# INPUT PARAMETERS


def fun3(a, b):
    """
    This function takes in two parameters ``a`` and ``b``
    and returns the sum of the two parameters.

    If we try calling this function without two parameters to it will
    throw an error.
    # wrong >> fun3()

    # correct >> fun3(1, 2)

    :param a:
    :param b:
    """
    print(a + b)


# ===============================================
# return values

def fun4(a, b):
    """
    A function can only have a single return value,
    but that value can be a list or tuple,
    so in practice you can return as many different values from a function as you like.
    :param a:
    :param b:

    """
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b

    return add, sub, mul, div


# ================================
# RECURSION

def fibonacci(n):

    """
    Everyone knows about fibonacci, well this is a simple program that
    shows how Recursion works.'

    the zeroth number is 0, the first number is 1,
    and each subsequent number is the sum of the previous two numbers.

    NOTE: Whenever we write a recursive function we need to ensure that
    the function terminates, that is we dont want a function that keeps on calling
    itself again and again.
    :param n:
    """

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

# to avoid recursion we write the function in an iterative way as shown below


def fibonacci2(n):
    current, next_ = 0, 1

    for i in range(n):
        current, next_ = next_, current + next_

    return current

# ==================================================================
# factorial of a number


def fact(n):

    current, next_ = 1, n

    for i in range(n):
        current, next_ = current * next_, next_ - 1

    return current

# =======================================================================
# Default Parameters

"""
Sometimes we have to make some parameters optional,
we achieve that by making them optional.
"""


def marital_status(fname, lname, status='Single', country='Kenya'):
    """
    The above function takes four parameters but
    two of them are necessary that is when you make
    a call to the function you must pass these params.
    Usage:
    ``necessary params``

    >>> marital_status('John', 'Doe')
    >>> 'John Doe is currently Single and lives in Kenya'

    Usage:
    ``passing optional params``

    >>> marital_status('John', 'Doe', 'Married', 'Madagascar')
    >>> 'John Doe is currently Married and lives in Madagascar'

    Note:
        Notice the difference when optional params are passed into the function.
    """
    full_name = '%s %s' % (fname, lname)
    if status is not 'Single':
        return '%s is currently %s and lives in %s' %(full_name, status, country)
    return '%s is currently %s and lives in %s' % (full_name, status, country)

# ===============================================================================
# *ARGS AND **KWARGS

"""
Sometimes we may want to pass a variable-length list of positional
or keyword parameters into a function. We can put * before a parameter name
to indicate that it is a variable-length tuple of positional parameters,
and we can use ** to indicate that a parameter is a variable-length dictionary
of keyword parameters.

By convention, the parameter name we use for the tuple is
``args`` and the name we use for the dictionary is ``kwargs``:

"""


def my_args(*args):
    """
    we can access args as a normal tuple, but the ``*``
    means that args isn't passed into the function as a single parameter
    which is a tuple:
    instead, it is passed in as a series of individual parameters
    usage:
        >>> a = [1,2,3,4,5]
        >>> my_args(*a)
            1
            2
            3
            4
            5

    """
    for arg in args:
        print(arg)


def my_kwargs(**kwargs):
    """
    ``**`` means that kwargs is passed in as a series of individual keyword parameters,
     rather than a single parameter which is a dictionary:

    usage:
        >>> my_dict = {
            '1': 1,
            '2': 2,
        }
        >>> my_kwargs(**my_dict)
            1: 1
            2: 2

    """
    for k, v in kwargs.items():
        print('{}: {}'.format(k, v))


# ====================================
# Decorators
"""
Lets write a simple decorator that returns a persons
full names.

"""


def my_decorator(func):
    def func_wrapper(full_name):
        return 'Your names are {0}'.format(func(full_name))
    return func_wrapper


@my_decorator
def get_full_names(full_name):
    return full_name

# Decorating methods


def my_method_decorator(func):
    def func_wrapper(*args, **kwargs):
        return 'Your names are {0}'.format(func(*args, **kwargs))
    return func_wrapper


class Names:
    def __init__(self):
        self.names = 'Gideon'

    @my_method_decorator
    def get_all_names(self):
        return self.names






