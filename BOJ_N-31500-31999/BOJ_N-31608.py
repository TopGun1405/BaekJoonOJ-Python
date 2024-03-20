def main():
    N = int(input())
    S = input()
    T = input()

    cnt = 0
    for s, t in zip(S, T):
        if s != t:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
