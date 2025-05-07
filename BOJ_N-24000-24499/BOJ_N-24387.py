def main():
    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()))

    P = 0
    for A_i, B_i in zip(A, B):
        P += A_i * B_i

    print(P)


if __name__ == "__main__":
    main()
