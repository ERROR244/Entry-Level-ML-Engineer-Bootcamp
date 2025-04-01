import sys
import string

def ft_filter(func, iterable):
    """
    Custom filter function that mimics the behavior of Python's built-in filter.
    Returns items of iterable for which func(item) is true.
    """
    return [item for item in iterable if func(item)]

def is_valid_word(word, n):
    word_without_punctuation = word.translate(str.maketrans('', '', string.punctuation))
    if len(word_without_punctuation) > n:
        return word
    return None

def main(S, N):
    if not isinstance(S, str) or not isinstance(N, int):
        print("Error: Invalid arguments.")
        return
    
    words = S.split()
    fWords = ft_filter(lambda word: is_valid_word(word, N), words)
    print(fWords)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error: Invalid number of arguments.")
    else:
        main(sys.argv[1], int(sys.argv[2]))

