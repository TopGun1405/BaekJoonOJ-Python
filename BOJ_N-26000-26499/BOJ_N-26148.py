def main():
    N = int(input())

    if N % 4 == 0:
        if N % 100 == 0:
            if N % 400 == 0:
                print(30)
            else:
                print(29)
        else:
            print(30)
    else:
        print(29)


if __name__ == "__main__":
    main()
