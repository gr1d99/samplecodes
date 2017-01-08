# vowels

vowels = 'aeiou'
count = 0

for i in vowels:
    count += 1

print(count)


def count_vowels(s):
    valid_vowels = 'aeiou'
    len_of_given_string = len(s)
    initial_count = len_of_given_string - 1
    count = 0
    if not isinstance(s, str):
        raise Warning('%s must be a string' %s)
    else:
        for i in range(len_of_given_string):
            if s[initial_count] in valid_vowels:
                count += 1
            if initial_count != 0:
                initial_count -= 1
        print('initial count has reached 0, exitting...')
        print(count)


# iters

def myiterator():
    x = 5
    ans = 0
    left = x
    while left != 0:
        ans += x
        left -= 1
        print('x is: ', x)
        print('ans is: ', ans)
        print('left is: ', left)

    print(str(x) + '*' + str(x) + '=' + str(ans))


def cube(x):
    ans = 0
    while ans**3 < x:
        ans += 1

    if ans**3 == x:
        print('The cube root of {} is {}'.format(x, ans))
    else:
        print(str(x) + ' is not a perfect root')


# cleaner

def clean_cube(x):
    for guess in range(x+1):
        if guess ** 3 == x:
            print('cube root of {} is {} '.format(x, guess))

s = None
valid_vowels = 'aeiou'
count = 0
if not isinstance(s, str):
    raise Warning('%s must be a string' %s)
else:
    len_of_given_string = len(s)
    initial_count = len_of_given_string - 1
    for i in range(len_of_given_string):
        if s[initial_count] in valid_vowels:
            count += 1
        if initial_count != 0:
            initial_count -= 1
    print(count)


# problem2
def problem2(my_string):
    occuring_string = 'bob'
    sliced_strings = []
    counter = 0
    my_string_length = len(my_string)
    my_string_starting_index = 0
    my_string_ending_index = 3
    for n in range(my_string_length):
        sliced_strings.append(my_string[my_string_starting_index:my_string_ending_index])
        my_string_starting_index += 1
        my_string_ending_index += 1
    for string in sliced_strings:
        if string == occuring_string:
            counter += 1
        else:
            continue
    print(counter)


s = 'azcbobobegghakl'

result = []
final = []

for letters in s:
    result += letters
    if result == sorted(result) and len(result) >= len(final):
        final = list(result)
    elif result != sorted(result):
        result = [result[len(result)-1]]
print("Longest substring in alphabetical order is: ".join(final))

