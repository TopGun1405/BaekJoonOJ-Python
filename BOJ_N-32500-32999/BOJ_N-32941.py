def main():
    T, X = map(int, input().split())
    N = int(input())
    t = {n: 0 for n in range(1, T+1)}
    for _ in range(N):
        K_i = int(input())
        A = list(map(int, input().split()))
        for A_i in A:
            t[A_i] += 1

    print("YES" if t[X] == N else "NO")


if __name__ == "__main__":
    main()
