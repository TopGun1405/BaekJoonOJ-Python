def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        ans, temp = 0, [1]
        for i in range(1, n + 1):
            temp[-1] += i + 1
            ans += i * temp[-1]
        print(ans)


if __name__ == "__main__":
    main()
