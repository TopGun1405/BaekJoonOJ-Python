def main():
    T = int(input())
    for t in range(1, T+1):
        N, M = map(int, input().split())
        print(f"Case {t}: {M - (N-1)}")


if __name__ == "__main__":
    main()
