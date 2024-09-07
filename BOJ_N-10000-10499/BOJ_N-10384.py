def main():
    T = int(input())

    alp = list(range(97, 123))
    for t in range(1, T+1):
        n = input().lower()

        c = [0] * 26
        for i in n:
            if ord(i) in alp:
                c[ord(i)-97] += 1

        if min(c) == 0:
            print(f"Case {t}: Not a pangram")
        elif min(c) == 1:
            print(f"Case {t}: Pangram!")
        elif min(c) == 2:
            print(f"Case {t}: Double pangram!!")
        elif min(c) == 3:
            print(f"Case {t}: Triple pangram!!!")


if __name__ == "__main__":
    main()
