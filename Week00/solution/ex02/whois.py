import sys

def pError(error):
    print(f"AssertionError: {error}")
    exit()

def EvenOdd(nbr):
    if nbr == 0:
        print("I'm Zero.")
    elif nbr%2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

l = len(sys.argv)
if l > 2:
    pError("more than one argument is provided")
elif l == 1:
    exit()


try:
    nbr = int(sys.argv[1])
    EvenOdd(nbr)
except:
    pError("argument is not an integer")