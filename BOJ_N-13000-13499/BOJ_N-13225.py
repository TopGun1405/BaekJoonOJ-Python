def main():
    C = int(input())
    for _ in range(C):
        n = int(input())
        cnt = 0
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                cnt += 1
                if i ** 2 != n:
                    cnt += 1
        print(n, cnt)


if __name__ == "__main__":
    main()
