def main():
    N = int(input())
    Swifts = list(map(int, input().split()))
    Semaphores = list(map(int, input().split()))

    idx = 0
    Sw, Se = 0, 0
    for i in range(N):
        Sw += Swifts[i]
        Se += Semaphores[i]

        if Sw == Se:
            idx = i + 1

    print(idx)


if __name__ == "__main__":
    main()
