def main():
    while True:
        a0 = input()
        if a0 == 0:
            break
        for _ in range(4):
            a0 = str(int(a0) ** 2)
            if len(a0) < 8:
                a0 = '0' * (8 - len(a0)) + a0
            a0 = a0[2:6]
        print(a0)


if __name__ == "__main__":
    main()
