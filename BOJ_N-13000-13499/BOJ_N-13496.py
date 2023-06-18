def main():
    K = int(input())
    for i in range(K):
        n, s, d = map(int, input().split())
        ans = 0
        for _ in range(n):
            di, vi = map(int, input().split())
            if d * s >= di:
                ans += vi
        print("Data Set {}:".format(i + 1))
        print(ans)
        print()


if __name__ == "__main__":
    main()
    