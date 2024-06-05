def main():
    N = int(input())
    A = list(map(int, input().split()))

    # score = 0
    # for i, A_i in enumerate(A):
    #     score += 180 * (A_i - 2)
    #     if i > 0:
    #         score += 180 * A_i - 180 * (A_i - 2)

    score = 180 * (A[0] - 2)
    for i in range(1, N):
        score += 180 * A[i]

    print(score)


if __name__ == "__main__":
    main()
