def main():
    while True:
        n = int(input())
        if n == 0:
            break
        a = list(map(int, input().split()))
        times = sorted(enumerate(map(lambda a_n: abs(2023 - a_n), a)), key=lambda k: k[1])
        print(times[0][0] + 1)


if __name__ == "__main__":
    main()
