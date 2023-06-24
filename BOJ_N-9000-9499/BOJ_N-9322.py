def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        K1 = input().split()
        K2 = input().split()
        C = input().split()

        P = {}
        for k in K2:
            P[K1.index(k)] = C.pop(0)
        print(*dict(sorted(P.items())).values())


if __name__ == "__main__":
    main()
