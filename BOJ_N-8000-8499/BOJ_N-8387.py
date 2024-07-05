def main():
    n = int(input())
    S1 = input()
    S2 = input()

    cnt = 0
    for c1, c2 in zip(S1, S2):
        if c1 == c2:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
