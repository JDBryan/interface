
def subtract(num_a, num_b):
    return num_a - num_b

def times(num_a, num_b, num_c):
    return num_a * num_b * num_c

def addition(num_a, num_b, num_c):
    return num_a + num_b + num_c

def divide(num_a, num_b):
    return num_a / num_b

def isTwoOrThree(num):
    if num == 2:
        print("Number is 2, YAY!")
    elif num == 3:
        print("Number is 3, YAY!")
    else:
        print("Number is not 2 or 3 :(")

def sum(number_list):
    total = 0
    for number in number_list:
        total = total + number
    return total

var_a = 10

list_a = [3, 4, 10, 7, 6, 8]
list_b = [1, 1, 1, 1, 1]

print(sum(list_b))

def add(number_list):
    total = 0
    for _ in number_list:
        total = total + 1
    return total

print(add(list_a))

        