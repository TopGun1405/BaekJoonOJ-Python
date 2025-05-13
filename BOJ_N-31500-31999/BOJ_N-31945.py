def main():
    T = int(input())
    for _ in range(T):
        P = sorted(map(int, input().split()))
        S = [
            [0, 1, 2, 3], [0, 1, 4, 5], [0, 2, 4, 6],
            [1, 3, 5, 7], [2, 3, 6, 7], [4, 5, 6, 7]
        ]
        print("YES" if P in S else "NO")


if __name__ == "__main__":
    main()
