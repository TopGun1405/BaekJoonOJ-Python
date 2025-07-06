def main():
    N = int(input())
    S = input()

    sp = "!@#$%^&*()-+"
    n = [1, 1, 1, 1]
    for c in S:
        k = ord(c)
        if 48 <= k <= 57:
            n[0] = 0
        elif 65 <= k <= 91:
            n[1] = 0
        elif 97 <= k <= 123:
            n[2] = 0
        elif c in sp:
            n[3] = 0
    N += sum(n)

    print(sum(n) + (0 if N > 6 else (6 - N)))


if __name__ == "__main__":
    main()
