def main():
    n = int(input())
    ans = n
    for i in range(2, int(n ** 0.5) + 1):
        for j in range(i, n):
            if i * j <= n:
                ans += 1
            else:
                break
    print(ans)


if __name__ == "__main__":
    main()
