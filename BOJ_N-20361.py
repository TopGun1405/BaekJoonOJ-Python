def main():
    N, X, K = map(int, input().split())
    ball = X
    for _ in range(K):
        A, B = map(int, input().split())
        if A == ball:
            ball = B
        elif B == ball:
            ball = A
    print(ball)


if __name__ == "__main__":
    main()
