def main():
    N, Q = map(int, input().split())
    sheet = [int(input()) for _ in range(N)]
    for _ in range(Q):
        t = int(input())
        for i in range(N):
            if t < sum(sheet[:i+1]):
                print(i + 1)
                break


if __name__ == "__main__":
    main()
