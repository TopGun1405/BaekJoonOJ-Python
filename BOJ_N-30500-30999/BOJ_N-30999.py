def main():
    N, M = map(int, input().split())
    votes = [list(input()) for _ in range(N)]
    cnt = 0
    for vote in votes:
        if vote.count("O") > M // 2:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
