def main():
    while True:
        try:
            N, B, M = map(float, input().split())
        except EOFError:
            break

        cnt = 0
        while M > N:
            N += N * B / 100
            cnt += 1

        print(cnt)


if __name__ == "__main__":
    main()
