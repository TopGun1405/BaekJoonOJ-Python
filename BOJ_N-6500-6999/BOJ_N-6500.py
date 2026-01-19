def main():
    n = 4
    while True:
        a0 = input()

        if a0 == "0":
            break

        rand, ai = {a0}, a0
        while True:
            ai = str(int(ai) ** 2)
            ai = ("0" * (2*n - len(ai)) + ai)[2:6]
            if ai in rand:
                break
            rand.add(ai)

        print(len(rand))


if __name__ == "__main__":
    main()
