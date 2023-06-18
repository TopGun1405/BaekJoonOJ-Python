def main():
    T = int(input())

    for _ in range(T):
        N = int(input())
        num = list(map(int, input().split()))
        print(sum(num))


if __name__ == "__main__":
    main()
