def main():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        ans = (m - n + 1) * (n + m) // 2
        print("Scenario #{}:".format(i + 1))
        print(ans)
        if i < t - 1:
            print()


if __name__ == "__main__":
    main()
