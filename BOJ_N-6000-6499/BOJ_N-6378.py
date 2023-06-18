def main():
    while True:
        num = list(map(int, list(input())))
        if num[0] == 0:
            break
        while len(num) > 1:
            num = list(map(int, str(sum(num))))
        print(num[0])


if __name__ == "__main__":
    main()
