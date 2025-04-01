# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)

from datetime import datetime


def main():
    dt = datetime(*kata)
    f = dt.strftime("%m/%d/%Y %H:%M")
    print(f"{f}")

if __name__ == "__main__":
    main()