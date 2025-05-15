def main():
    N = int(input())
    A = int(input())
    B = int(input())

    cnt = 0
    for n in range(1, N+1):
        if (n % A == 0 and n % B != 0) or (n % A != 0 and n % B == 0):
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
