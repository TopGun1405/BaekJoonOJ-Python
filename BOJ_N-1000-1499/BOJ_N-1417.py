def main():
    N = int(input())
    D = int(input())
    votes = sorted([int(input()) for _ in range(N-1)])

    cnt = 0
    if N == 1:
        print(0)
    else:
        while votes[-1] >= D:
            D += 1
            votes[-1] -= 1
            cnt += 1
            votes.sort()
        print(cnt)


if __name__ == "__main__":
    main()
