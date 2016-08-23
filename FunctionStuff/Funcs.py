def some_notes():
    notes = """
    A function is asequence of statements which perfom some kind of a task.
    We mostly use functions to eliminate code duplication.

    Python has some inbuilt functions, some of them are
        : ``print``
        : ``len``
    """

    print(notes)

# ------------------------------------------------------------------------------------


def fun1():
    """
    Because defining a function does not cause it to execute,
    we can use an identifier inside a function even if it hasn't been defined yet
     – as long as it becomes defined by the time we run the function.

    : fun()1 calls fun2()
    """
    fun2()


def fun2():
    print("hey i'm fun2() and I was just called by another function up there.")

# try moving fun2() above fun1() and see if the code will run

# -----------------------------------------------------------------------------------

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


# ---------------------------------------------------------------------

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









