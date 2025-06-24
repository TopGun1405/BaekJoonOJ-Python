def main():
    N = int(input())
    X, Y, R = map(int, input().split())
    T = [int(input()) for _ in range(N)]

    A, B = 0, 0
    left, right = X-R, X+R
    for T_i in T:
        if left < T_i < right:
            A += 1
        elif T_i == left or T_i == right:
            B += 1

    print(A, B)


if __name__ == "__main__":
    main()
