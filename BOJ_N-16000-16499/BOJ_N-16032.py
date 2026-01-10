def main():
    while True:
        n = int(input())
        if n == 0:
            break
        a = list(map(int, input().split()))

        avg = sum(a) / n

        print(len(list(filter(lambda e: e <= avg, a))))


if __name__ == "__main__":
    main()
