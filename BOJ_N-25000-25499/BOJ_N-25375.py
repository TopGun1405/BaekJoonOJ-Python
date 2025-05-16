def main():
    Q = int(input())
    for _ in range(Q):
        a, b = map(int, input().split())

        print(1 if b % a == 0 and b // a >= 2 else 0)


if __name__ == "__main__":
    main()
