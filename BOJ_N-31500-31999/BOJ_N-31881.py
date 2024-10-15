def main():
    N, Q = map(int, input().split())

    virus = [0] * (N+1)
    computer = N
    for _ in range(Q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            x = query[1]
            if not virus[x]:
                computer -= 1
            virus[x] = 1

        elif query[0] == 2:
            x = query[1]
            if virus[x]:
                computer += 1
            virus[x] = 0

        else:
            print(computer)


if __name__ == "__main__":
    main()
