def main():
    N, K = map(int, input().split())
    S = input()

    if K == 1:
        GText = S
    elif (N - K) % 2:
        GText = S[K-1:] + S[:K-1]
    else:
        GText = S[K-1:] + S[K-1::-1]

    print(GText)


if __name__ == "__main__":
    main()
