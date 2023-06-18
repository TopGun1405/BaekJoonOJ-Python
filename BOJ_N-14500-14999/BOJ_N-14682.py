def main():
    N = int(input())
    k = int(input())
    ans = 0
    for n in range(k + 1):
        ans += N * (10 ** n)
    print(ans)


if __name__ == "__main__":
    main()
