def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print("YES" if sum((n + 1) // 2 for n in A) >= N else "NO")


if __name__ == "__main__":
    main()
