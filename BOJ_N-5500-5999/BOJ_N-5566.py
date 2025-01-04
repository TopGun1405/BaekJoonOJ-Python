def main():
    N, M = map(int, input().split())
    cmd = [int(input()) for _ in range(N)]

    dice = 0
    for i in range(1, N):
        dice += int(input())

        if dice >= N-1:
            print(i)
            break

        dice += cmd[dice]

        if dice >= N-1:
            print(i)
            break


if __name__ == "__main__":
    main()
