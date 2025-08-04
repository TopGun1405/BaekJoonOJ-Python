def main():
    N = input()

    k, cnt = len(N), 0
    while True:
        N = str(int(N) * 2)

        if len(N) != k:
            print(cnt)
            break

        cnt += 1
        k = len(N)


if __name__ == "__main__":
    main()
