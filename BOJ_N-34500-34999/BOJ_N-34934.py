def main():
    N = int(input())
    s = [input().split() for _ in range(N)]

    s.sort(key=lambda k: k[1])

    print(s[-1][0])


if __name__ == "__main__":
    main()
