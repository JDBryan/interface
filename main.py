
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

print(sum(list_a))

def numbersize(num):
    if num < 11:
        print("small")
    elif num < 21:
        print ("medium")
    else:
        print("Big")


numbersize(15)
numbersize(3)
numbersize(39)

def fiftyorsixty(num):
    if num <= 60 and num >= 50:
        print("yes")
    else:
        print("NO")
    
fiftyorsixty(50)
fiftyorsixty(60)
fiftyorsixty(57)
fiftyorsixty(28)
fiftyorsixty(9000)