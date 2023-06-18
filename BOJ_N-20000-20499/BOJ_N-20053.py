def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        num = sorted(map(int, input().split()))
        print(num[0], num[-1])


if __name__ == "__main__":
    main()
