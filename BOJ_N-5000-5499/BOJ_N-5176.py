def main():
    K = int(input())
    for _ in range(K):
        P, M = map(int, input().split())
        wants = [int(input()) for _ in range(P)]
        if M == 1:
            print(P - 1)
        else:
            ans = 0
            for i in range(1, M + 1):
                if wants.count(i) >= 2:
                    ans += wants.count(i) - 1
            print(ans)


if __name__ == "__main__":
    main()
