def main():
    while True:
        num = input()
        if num == '0':
            break
        dec = 0
        facto = [1, 1, 2, 6, 24, 120]
        for i, v in enumerate(num):
            dec += int(v) * facto[len(num) - i]
        print(dec)


if __name__ == "__main__":
    main()
