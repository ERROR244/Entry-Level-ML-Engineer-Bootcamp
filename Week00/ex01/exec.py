import sys


def revAndPrint(str: str):
    str = str[::-1]
    print(str.swapcase())
        

if (len(sys.argv) == 1):
    exit(0)
elif (len(sys.argv) == 2):
    revAndPrint(sys.argv[1])
else:
    revAndPrint(' '.join(sys.argv[1:]))
