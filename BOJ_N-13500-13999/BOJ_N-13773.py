def main():
    while True:
        Y = int(input())

        if Y == 0:
            break

        if 1896 <= Y and Y % 4 == 0:
            if 1914 <= Y <= 1918 or 1939 <= Y <= 1945:
                print(Y, "Games cancelled")
            elif 2020 < Y:
                print(Y, "No city yet chosen")
            else:
                print(Y, "Summer Olympics")
        else:
            print(Y, "No summer games")


if __name__ == "__main__":
    main()
