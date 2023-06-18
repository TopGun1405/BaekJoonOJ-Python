def main():
    N = input()
    i = len(N) // 2
    a = b = 0
    for n in N[:i]:
        a += int(n)
    for n in N[i:]:
        b += int(n)
    print("LUCKY" if a == b else "READY")


if __name__ == "__main__":
    main()
