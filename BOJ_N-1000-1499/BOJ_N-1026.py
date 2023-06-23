def main():
    N = int(input())
    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()), reverse=True)
    S = 0
    for a, b in zip(A, B):
        S += a * b
    print(S)


if __name__ == "__main__":
    main()
