def main():
    C, K, P = map(int, input().split())
    tot = 0
    for i in range(1, C + 1):
        tot += (K * i + P * (i ** 2))
    print(tot)


if __name__ == "__main__":
    main()
