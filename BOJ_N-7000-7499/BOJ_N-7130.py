def main():
    M, H = map(int, input().split())
    N = int(input())

    happy = 0
    for _ in range(N):
        C, B = map(int, input().split())
        happy += max(C * M, B * H)

    print(happy)


if __name__ == "__main__":
    main()
