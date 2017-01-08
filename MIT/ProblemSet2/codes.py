def intrest_calc():
    """
    Monthly interest rate= (Annual interest rate) / 12.0
    Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
    Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
    :return:
    """
    count = 0
    while(count > 12):
        balance = 42
        annualInterestRate = 0.2
        monthlyPaymentRate = 0.04
        updated_bal_each_mon = None
        count += 1
        prev_bal = balance
        min_mon_pay = monthlyPaymentRate * prev_bal
        mon_unpaid_bal = prev_bal - min_mon_pay
        updated_bal_each_mon = mon_unpaid_bal + ((annualInterestRate/12.0) * mon_unpaid_bal)
        balance = prev_bal
        print(updated_bal_each_mon, count, balance)

    print(updated_bal_each_mon)


def strings_stuff():
    an_letters = 'aefhilmnorsxAEFHILMNORSX'

    word = input("I will cheer for you! Enter a word: ")
    times = int(input('Enthusiasm level (1-10): '))
    i = 0

    while i < len(word):
        char = word[i]
        if char in an_letters:
            print('Give me an ' + char + '! ' + char)
        else:
            print('Give me a ' + char + '! ' + char)
        i += 1

    print("What does that spell? ")
    for i in range(times):
        print(word, "!!!")


def bisection_search():
    sqr_num = int(input("Enter a number that you would like to find its square root: "))
    epsilon = 0.01
    count = 0
    low = 1.0
    high = sqr_num

    ans = (high + low)/2

    while abs(ans ** 2 - sqr_num) >= epsilon:
        print("high is {}, low is {}, and ans is {} ".format(high, low, ans))
        count += 1

        if ans ** 2 < sqr_num:
            low = ans

        else:
            high = ans

        ans = (high + low)/2

    print('loop lasted {} times and {} is close to the square root of {}'.format(count, ans, sqr_num))


def t(aTuple):
    a = ()
    b = ()

    for i in aTuple:
        print(i[0])



