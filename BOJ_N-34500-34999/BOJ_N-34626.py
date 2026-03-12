def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        print(1 + (len(set(a)) - 1) * 2)


if __name__ == "__main__":
    main()
