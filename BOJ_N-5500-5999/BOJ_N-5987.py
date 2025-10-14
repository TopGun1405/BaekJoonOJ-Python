def main():
    Z = int(input())
    for _ in range(Z):
        N_i, C_i, str_i = input().split()
        N_i, C_i = int(N_i), int(C_i)

        for _ in range(C_i):
            str_i = str_i[N_i:] + str_i

        print(str_i)


if __name__ == "__main__":
    main()
