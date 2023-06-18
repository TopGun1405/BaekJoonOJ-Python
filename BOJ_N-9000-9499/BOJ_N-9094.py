def main():
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        num = list(range(1, n))
        pair = 0
        for i in range(len(num) - 1):
            for j in range(i + 1, len(num)):
                r = (num[i] ** 2 + num[j] ** 2 + m) / (num[i] * num[j])
                if int(r) == r:
                    pair += 1
        print(pair)


if __name__ == "__main__":
    main()
