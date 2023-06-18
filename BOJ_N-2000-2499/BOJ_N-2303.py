def main():
    N = int(input())
    o = []
    for i in range(N):
        o.append([i + 1, sum(sorted(map(int, input().split()))[:-3]) % 10])
    o.sort(key=lambda k: k[1])
    print(o[0])


if __name__ == "__main__":
    main()
