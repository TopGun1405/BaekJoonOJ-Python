def main():

    def backtracking():
        if len(seq) == N:
            print(" ".join(map(str, seq)))
            return
        for n in range(1, N + 1):
            if n in seq:
                continue
            seq.append(n)
            backtracking()
            seq.pop()

    N = int(input())
    seq = []
    backtracking()


if __name__ == "__main__":
    main()
