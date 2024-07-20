def main():
    S = input()

    cnt = 1
    for c1, c2 in zip(S[:-1], S[1:]):
        if ord(c1) >= ord(c2):
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
