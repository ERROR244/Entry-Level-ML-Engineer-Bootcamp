# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)


def main():
    print(f"module_{(str(kata[0]) if kata[0] > 9 else f'0{str(kata[0])}')}, ", end="")
    print(f"ex_{(str(kata[1]) if kata[1] > 9 else f'0{str(kata[1])}')} : ", end="")
    print(f"{kata[2]:.2f}, ", end="")
    print(f"{kata[3]:.2e}, ", end="")
    print(f"{kata[4]:.2e}, ")

if __name__ == "__main__":
    main()