def main():
    S0, N, M = map(int, input().split())
    maxL, elements = S0, 0
    for _ in range(N + M):
        cmd = int(input())
        if cmd:
            elements += 1
            if maxL < elements:
                maxL *= 2
        else:
            elements -= 1
    print(maxL)


if __name__ == "__main__":
    main()
