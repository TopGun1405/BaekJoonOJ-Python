def main():
    N, C, S = map(int, input().split())
    X = list(map(int, input().split()))

    pos, cnt = 1, 0 if S != 1 else 1
    for X_C in X:
        if X_C == 1:
            pos += 1
            if pos > N:
                pos = 1
        else:
            pos -= 1
            if pos < 1:
                pos = N

        if pos == S:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
