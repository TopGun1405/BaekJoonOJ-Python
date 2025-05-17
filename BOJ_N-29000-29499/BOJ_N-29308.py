def main():
    n = int(input())
    p = [list(map(lambda e: int(e) if e.isdigit() else e, input().split())) for _ in range(n)]

    p = sorted((filter(lambda e: e[2] == "Russia", p)))

    print(p[-1][1])


if __name__ == "__main__":
    main()
