def main():
    N, M = map(int, input().split())
    tickets = [int(input()) for _ in range(N)]
    for i in range(1, M + 1):
        for j in range(1, N):
            if tickets[j - 1] % i > tickets[j] % i:
                tickets[j - 1], tickets[j] = tickets[j], tickets[j - 1]
    print(*tickets, sep='\n')


if __name__ == "__main__":
    main()
