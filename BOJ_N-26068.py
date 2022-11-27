def main():
    N = int(input())
    ans = 0
    for _ in range(N):
        leftDays = int(input()[2:])
        if leftDays <= 90:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
