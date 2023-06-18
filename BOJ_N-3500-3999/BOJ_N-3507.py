def main():
    n = int(input())
    if n > 198:
        print(0)
    else:
        ans = 0
        for i in range(100):
            for j in range(100):
                if n - i - j == 0:
                    ans += 1
        print(ans)


if __name__ == "__main__":
    main()
