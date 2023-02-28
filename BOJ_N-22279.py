def main():
    N = int(input())
    ans = 0
    for _ in range(N):
        q, y = map(float, input().split())
        ans += q * y
    print("{:0.3f}".format(ans))


if __name__ == "__main__":
    main()
