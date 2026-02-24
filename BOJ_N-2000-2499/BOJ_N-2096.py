def main():
    N = int(input())
    a = list(map(int, input().split()))

    # i행 j열에 도착할 때 얻을 수 있는 최소/최대 점수
    min_dp, max_dp = a[:], a[:]
    for _ in range(N-1):
        a = list(map(int, input().split()))

        prev_min, prev_max = min_dp[:], max_dp[:]

        # i행 0열(a[0])에 도착할 수 있는 경우: (i-1)행 0/1열
        # i행 1열(a[1])에 도착할 수 있는 경우: (i-1)행 0/1/2열
        # i행 2열(a[2])에 도착할 수 있는 경우: (i-1)행 1/2열
        min_dp[0] = min(prev_min[0], prev_min[1]) + a[0]
        min_dp[1] = min(prev_min[0], prev_min[1], prev_min[2]) + a[1]
        min_dp[2] = min(prev_min[1], prev_min[2]) + a[2]

        max_dp[0] = max(prev_max[0], prev_max[1]) + a[0]
        max_dp[1] = max(prev_max[0], prev_max[1], prev_max[2]) + a[1]
        max_dp[2] = max(prev_max[1], prev_max[2]) + a[2]

    print(max(max_dp), min(min_dp))


if __name__ == "__main__":
    main()
