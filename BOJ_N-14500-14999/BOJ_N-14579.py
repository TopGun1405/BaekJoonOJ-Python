def main():
    a, b = map(int, input().split())
    ans = 1
    for i in range(a, b + 1):
        ans *= sum(range(1, i + 1))
    print(ans % 14579)


if __name__ == "__main__":
    main()
