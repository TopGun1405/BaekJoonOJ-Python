def main():
    N = int(input())
    weather = list(map(int, input().split()))

    rage = [0] * N
    rage[0] = 1 if weather[0] == 1 else -1
    for i in range(1, N):
        if weather[i] == 1:
            rage[i] = rage[i-1] + 1
        else:
            rage[i] = rage[i-1] - 1

    print(sum(rage))


if __name__ == "__main__":
    main()
