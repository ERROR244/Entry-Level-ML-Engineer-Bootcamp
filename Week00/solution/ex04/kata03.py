# Put this at the top of your kata03.py file
kata = "The right format"


def main():
    print(f"{'-' * (41 - len(kata))}{kata}")

if __name__ == "__main__":
    main()