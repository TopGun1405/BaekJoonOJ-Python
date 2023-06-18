def main():
    N = int(input())
    P = list(map(int, input().split()))
    n, size = 0, []
    for i in range(N - 1):
        if P[i] < P[i + 1]:
            n += P[i + 1] - P[i]
        else:
            size.append(n)
            n = 0
    size.append(n)
    print(max(size))


if __name__ == "__main__":
    main()
