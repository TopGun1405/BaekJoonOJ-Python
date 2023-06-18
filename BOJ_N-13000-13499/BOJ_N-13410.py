def main():
    N, K = map(int, input().split())
    gugu = list(map(lambda n: str(n)[::-1], [N * k for k in range(1, K + 1)]))
    print(max(list(map(int, gugu))))


if __name__ == "__main__":
    main()
