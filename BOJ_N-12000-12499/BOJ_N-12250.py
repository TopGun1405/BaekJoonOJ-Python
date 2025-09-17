def main():
    T = int(input())
    for x in range(1, T+1):
        A, B, K = map(int, input().split())

        y = 0
        for i in range(A):
            for j in range(B):
                if (i & j) < K:
                    y += 1

        print(f"Case #{x}: {y}")


if __name__ == "__main__":
    main()
