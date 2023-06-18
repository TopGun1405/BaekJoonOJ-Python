def main():
    N = int(input())
    A = int(''.join(input().split()), 2)
    cnt = 0
    print(A)
    ans = ''
    print(bin(A) << 1)
    while A != 0:
        A = min(A << 1, A >> 1)
        print(A << 1, A >> 1)
        cnt += 1
    print(ans)


if __name__ == "__main__":
    main()
