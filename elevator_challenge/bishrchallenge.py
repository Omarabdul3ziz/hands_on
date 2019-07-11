import random

left = random.randint(0,2)
right = random.randint(0,2)
current = input("Your current floor : ")

def get_elevator(left, right, current):

    a = abs(int(left) - int(current))
    b = abs(int(right) - int(current))
    if a>b :
        print ("the left elevator on the way")
    elif b>a :
        print ("the right elevator on the way")
    else:
        print ("the right elevator on the way")
get_elevator(left, right, current)

#thnx for the challenge ya alby :D
