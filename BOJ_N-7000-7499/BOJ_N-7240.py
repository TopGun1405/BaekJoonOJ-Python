def main():
    N, S = map(int, input().split())

    v = 0
    for i in range(N):
        a_i = int(input())
        if v > S:
            v -= 1
        v += a_i

    print(v)


if __name__ == "__main__":
    main()
