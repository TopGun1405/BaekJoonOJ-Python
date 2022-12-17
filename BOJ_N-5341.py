def main():
    while True:
        n = int(input())
        if n == 0:
            break
        ans = 0
        for i in range(n):
            ans += i + 1
        print(ans)


if __name__ == "__main__":
    main()
