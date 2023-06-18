def main():
    I = int(input())
    ans = 0
    for n in range(1, int(I ** 0.5) + 1):
        if I % n == 0:
            ans += n
            if n ** 2 != I:
                ans += I // n
    print(ans)


if __name__ == "__main__":
    main()
