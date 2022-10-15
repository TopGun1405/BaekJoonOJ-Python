def main():
    N = int(input())
    t = sorted(map(int, input().split()))
    tot, temp = 0, 0
    for i in range(N):
        tot += temp + t[i]
        temp += t[i]
    print(tot)


if __name__ == "__main__":
    main()
