def main():
    N, Q = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    for _ in range(Q):
        S_j, E_j = map(int, input().split())
        print(sum(H[S_j-1:E_j]))


if __name__ == "__main__":
    main()
