def main():
    N = int(input())

    bucket_list = [0] * 1_001
    for _ in range(N):
        s_i, t_i, b_i = map(int, input().split())
        bucket_list[s_i] += b_i
        bucket_list[t_i] -= b_i

    total_bucket, max_bucket = 0, 0
    for bucket in bucket_list:
        total_bucket += bucket
        max_bucket = max(max_bucket, total_bucket)

    print(max_bucket)


if __name__ == "__main__":
    main()
