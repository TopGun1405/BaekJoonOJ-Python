def main():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        c = list(map(int, input().split()))
        g = 0
        for i in c:
            g += i // K
        print(g)


if __name__ == "__main__":
    main()
