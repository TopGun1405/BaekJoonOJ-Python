def main():
    N = int(input())
    votes = list(map(int, input().split()))
    result = {-1: 0, 0: 0, 1: 0}
    for v in votes:
        result[v] += 1
    n = len(votes) // 2 + (1 if len(votes) % 2 else 0)
    print("INVALID" if result[0] >= n else "APPROVED" if result[1] > result[-1] else "REJECTED")


if __name__ == "__main__":
    main()
