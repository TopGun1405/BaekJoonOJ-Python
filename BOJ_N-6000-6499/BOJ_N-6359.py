def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        ans = 0
        for i in range(1, n):
            if i ** 2 <= n:
                ans += 1
            else:
                break
        print(ans)


if __name__ == "__main__":
    main()
