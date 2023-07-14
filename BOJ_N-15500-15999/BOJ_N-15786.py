def main():
    N, M = map(int, input().split())
    S = input()
    for _ in range(M):
        P = input()
        idx = 0
        for p in P:
            if S[idx] == p:
                idx += 1
            if idx == N:
                print("true")
                break
        else:
            print("true" if idx == N else "false")


if __name__ == "__main__":
    main()
