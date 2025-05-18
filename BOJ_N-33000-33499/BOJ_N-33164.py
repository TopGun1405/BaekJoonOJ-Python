def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    tot = 0
    for A_n in A:
        for B_m in B:
            tot += (A_n + B_m) * max(A_n, B_m)

    print(tot)


if __name__ == "__main__":
    main()
