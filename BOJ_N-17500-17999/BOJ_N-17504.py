def main():
    N = int(input())
    a = list(map(int, input().split()))
    P, Q = 1, a[-1]
    for ai in a[::-1][1:]:
        P += Q * ai
        P, Q = Q, P
    print(Q - P, Q)


if __name__ == "__main__":
    main()
