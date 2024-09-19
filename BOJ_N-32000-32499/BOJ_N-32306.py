def main():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    S1, S2 = 10*A[0] + 20*A[1] + 30*A[2], 10*B[0] + 20*B[1] + 30*B[2]
    print(1 if S1 > S2 else (2 if S2 > S1 else 0))


if __name__ == "__main__":
    main()
