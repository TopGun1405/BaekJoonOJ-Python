def main():
    N = int(input())
    M = int(input())
    broken = {} if M == 0 else set(map(int, input().split()))
    minC = abs(N - 100)
    for num in range(1_000_000):
        num = str(num)
        for n in num:
            if int(n) in broken:
                break
        else:
            minC = min(minC, abs(N - int(num)) + len(num))
    print(minC)


if __name__ == "__main__":
    main()
