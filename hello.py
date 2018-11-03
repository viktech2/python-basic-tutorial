print("Hello World !")
print("*" * 10)

message = """
    Hi "there,

    How are you ?

    Thanks
"""

print(message)

lang = "Python"

print(lang[0:2])
print(lang[1:-1])

fname = "Vikash"
lname = "shaw"
name = f"{fname} {lname}"
print(name)


print(10 / 3)  # return decimal
print(10 // 3)  # return integer
# print "ABC"

print(ord("b"))
# ternary
age = 18
msg = "Eligible" if age >= 18 else "Not eligible"
print(msg)


if 18 <= age < 65:
    print("eligible1")

a = 'hello'
print(set(a))
print(list(a))
print(tuple(a))

# Dictionary
state_capitals = {
    'Arkansas': 'Little Rock',
    'Colorado': 'Denver',
    'California': 'Sacramento',
    'Georgia': 'Atlanta'
}


for k in state_capitals.keys():
    #print('{} is the capital of {}'.format(state_capitals[k], k))
    print(f"{state_capitals[k]} is the capital of {k}")


""" command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command) """

# abc
""" while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break """


for number in range(1, 10):
    if number % 2 == 0:
        print(number)
else:
    print("we have 4 even numbers")


# *arguements
def multiply(*numbers):
    # print(numbers)
    total = 1
    for number in numbers:
        total *= number
    return total


print("start")
print(multiply(2, 3, 4, 5))


# **args
def save_user(**user):
    print(user)
    print(user['name'])


# keyword arguements
save_user(id=1, name="john", age=22)
