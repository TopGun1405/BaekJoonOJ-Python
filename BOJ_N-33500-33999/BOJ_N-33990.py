def main():
    N = int(input())
    RM1 = -1
    for _ in range(N):
        A_i, B_i, C_i = map(int, input().split())
        if A_i + B_i + C_i >= 512:
            if RM1 == -1:
                RM1 = A_i + B_i + C_i
            else:
                RM1 = min(RM1, A_i + B_i + C_i)

    print(RM1)


if __name__ == "__main__":
    main()
