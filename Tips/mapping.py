"""
Did you know that you can apply a function
to every item of iterable and return a list
of results, well it is pretty simple.

In the example below i'l create a function that
will multiply each argument passed to it by 10.

"""


def get_user_list():
    user_list = input('Please enter a sequence of numbers separated by a comma \n'
                          'eg. 1,2,3,4,5\n')

    num_list = []
    for n in user_list:
        num_list.append(int(n))
    print(type(num_list))


def generate_list_from_user_input(user_list):
    custom_list = []
    custom_list.extend(user_list)
    return custom_list


def multiply(x):
    return x * 10


def main_program(custom_list):
    return map(multiply, custom_list)


# i = get_user_list()
# c_l = generate_list_from_user_input(i)
# print main_program(c_l)


