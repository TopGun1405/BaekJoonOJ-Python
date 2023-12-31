def main():

    def backtracking():
        if len(seq) == M:
            print(" ".join(map(str, seq)))
            return
        for num in nums:
            seq.append(num)
            backtracking()
            seq.pop()

    N, M = map(int, input().split())
    nums = sorted(map(int, input().split()))
    seq = []
    backtracking()


if __name__ == "__main__":
    main()
