def main():
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    score = [0] * N
    for i in range(3):
        for j in range(N):
            for k in range(N):
                if j != k and nums[j][i] == nums[k][i]:
                    break
            else:
                score[j] += nums[j][i]
    print(*score, sep='\n')


if __name__ == "__main__":
    main()
