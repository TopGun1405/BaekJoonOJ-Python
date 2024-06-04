def main():
    N = int(input())
    T = [list(map(int, input().split())) for _ in range(N)]

    T = sorted(map(lambda e: sum(e[1:]), T))
    tmp, tot = 0, 0
    for t in T:
        tmp += t
        tot += tmp

    print(tot)


if __name__ == "__main__":
    main()
