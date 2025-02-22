
import sys

def pError(error):
    """
    print an error.
    Args:
        error (str): The error to print.
    Returns:
        none.
    """

    print(f"AssertionError: {error}")
    exit()

def text_analyzer(s = None):
    """
    Count the occurrences of different character types in a string.
    Args:
        s (str): Input string.
    Returns:
        none.
    """
    if s == None:
        s = input("What is the text to analyze?\n") + ' '
    if not isinstance(s, str):
        print("text_analyzer takes a string data type")
        return 

    p = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    l = len(s)
    print(f'The text contains {l} character(s): ')
    print(f'{sum(1 for c in s if c.isupper())} upper letter(s)')
    print(f'{sum(1 for c in s if c.islower())} lower letter(s)')
    print(f'{sum(1 for c in s if c in p)} punctuation mark(s)')
    print(f'{sum(1 for c in s if c.isspace())} space(s)')




def main(argv):
    l = len(argv)

    if l == 0:
        text_analyzer()
    elif l == 1:
        text_analyzer(argv[0])
    else:
        pError("more than one argument is provided")


if __name__ == "__main__":
    main(sys.argv[1:])

