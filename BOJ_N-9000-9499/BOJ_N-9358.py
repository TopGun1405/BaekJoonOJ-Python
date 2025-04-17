def main():
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        seq = list(map(int, input().split()))

        while len(seq) > 2:

            tmp = []
            for i in range(N//2):
                tmp.append(seq[i] + seq[-i-1])

            if N % 2:
                tmp.append(seq[N//2] * 2)

            N = N // 2 + (1 if N % 2 else 0)
            seq = tmp

        print(f"Case #{t}: {'Alice' if seq[0] > seq[1] else 'Bob'}")


if __name__ == "__main__":
    main()
