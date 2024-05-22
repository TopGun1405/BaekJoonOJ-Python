def main():
    N = int(input())
    ropes = sorted([int(input()) for _ in range(N)])

    maxW = 0
    for rope in ropes:
        maxW = max(rope * N, maxW)
        N -= 1
    print(maxW)


if __name__ == "__main__":
    main()
