def main():
    while True:
        num = input()

        if num == '0':
            break

        if num == num[::-1]:
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    main()
