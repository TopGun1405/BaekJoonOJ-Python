def main():
    N = int(input())
    T = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    lose = []
    for b_j in b:
        k = b_j % (2 * N) - 1
        a = a[k:] + a[:k]
        lose.append(a[0])

    print(*lose)


if __name__ == "__main__":
    main()
