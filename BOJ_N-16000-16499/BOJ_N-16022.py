def main():
    N = int(input())
    V = sorted([int(input()) for _ in range(N)])

    minSize = 1e9
    for i in range(1, N-1):
        left = V[i] - (V[i] + V[i-1])/2
        right = (V[i+1] + V[i])/2 - V[i]
        minSize = min(minSize, left + right)

    print(minSize)


if __name__ == "__main__":
    main()
