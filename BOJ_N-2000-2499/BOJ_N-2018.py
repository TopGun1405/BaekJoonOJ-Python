def main():
    N = int(input())

    end, tot, cnt = 0, 0, 0
    for start in range(N):
        while tot < N and end < N:
            tot, end = tot + end + 1, end + 1
        if tot == N:
            cnt += 1
        tot -= start + 1

    print(cnt)


if __name__ == "__main__":
    main()
