def main():
    T = int(input())
    for _ in range(T):
        N, M = input().split()

        cnt0, cnt1 = 0, 0
        for n, m in zip(N, M):
            if n != m:
                if m == '0':
                    cnt0 += 1
                else:
                    cnt1 += 1

        print(max(cnt0, cnt1))


if __name__ == "__main__":
    main()
