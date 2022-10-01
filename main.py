
def subtract(num_a, num_b):
    return num_a - num_b

def times(num_a, num_b):
    return num_a * num_b

def addition(num_a, num_b, num_c):
    return num_a + num_b + num_c

def isTwoOrThree(num):
    if num == 2:
        print("Number is 2, YAY!")
    elif num == 3:
        print("Number is 3, YAY!")
    else:
        print("Number is not 2 or 3 :(")


isTwoOrThree(addition(1, 1, 1))
isTwoOrThree(2)
isTwoOrThree(4)