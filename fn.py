"""1. Write a function for checking the speed of drivers. This function should have one parameter: speed.

    If speed is less than 70, it should print “Ok”.
    Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
    If the driver gets more than 12 points, the function should print: “License suspended”
"""


def check_speed(speed):
    points = 0
    if speed < 70:
        print("Ok")
    if speed >= 70:
        new_speed = speed - 70
        points = new_speed // 5
        if points < 12:
            print(f"Points:{points}")
        else:
            print("License Suspended")


# check_speed(72)


"""2. Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. For example, if the limit is 3, it should print:

    0 EVEN
    1 ODD
    2 EVEN
    3 ODD
"""


def showNumbers(limit):
    for number in range(0, limit+1):
        if(number % 2 == 0):
            print(f"{number} EVEN")
        else:
            print(f"{number} ODD")


# showNumbers(3)

"""
3. Write a function called show_stars(rows).
If rows is 5, it should print the following:

    *
    **
    ***
    ****
    *****
"""


def show_stars(rows):
    for row in range(1, rows+1):
        print("*" * row)
        # print("*"*f"{row}")


# show_stars(5)


# 4. Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.

def prime_numbers(limit):
    for num in range(0, limit + 1):
       # prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)


prime_numbers(10)
