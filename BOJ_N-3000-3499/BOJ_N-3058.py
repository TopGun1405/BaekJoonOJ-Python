def main():
    T = int(input())
    for _ in range(T):
        num = list(map(int, input().split()))
        t = []
        for n in num:
            if n % 2 == 0:
                t.append(n)
        print(sum(t), min(t))


if __name__ == "__main__":
    main()
