def main():
    f = input()
    N = int(input())
    c = 0
    for _ in range(N):
        ring = input()
        ring += ring
        if f in ring:
            c += 1
    print(c)


if __name__ == "__main__":
    main()
