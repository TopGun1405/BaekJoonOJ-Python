from itertools import combinations


def main():
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))

    cnt = 0
    for pairs in combinations(nums, 2):
        if sum(pairs) == K:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
