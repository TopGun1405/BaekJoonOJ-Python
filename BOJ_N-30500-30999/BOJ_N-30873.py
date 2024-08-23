def main():
    N = int(input())
    X = 0
    for _ in range(N):
        P_i, C_i = map(int, input().split())
        if abs(P_i - X) <= C_i:
            X += 1
        else:
            continue

    print(X)


if __name__ == "__main__":
    main()
