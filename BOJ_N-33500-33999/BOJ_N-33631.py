def main():
    F_s, C_s, E_s, B_s = map(int, input().split())
    F_n, C_n, E_n, B_n = map(int, input().split())
    Q = int(input())

    cookies = 0
    for _ in range(Q):
        n, i = map(int, input().split())

        if n == 1:
            maxC = min(F_s//F_n, C_s//C_n, E_s//E_n, B_s//B_n)
            if maxC >= i:
                F_s, C_s, E_s, B_s = F_s-F_n*i, C_s-C_n*i, E_s-E_n*i, B_s-B_n*i
                cookies += i
                print(cookies)
            else:
                print("Hello, siumii")

        elif n == 2:
            F_s += i
            print(F_s)

        elif n == 3:
            C_s += i
            print(C_s)

        elif n == 4:
            E_s += i
            print(E_s)

        elif n == 5:
            B_s += i
            print(B_s)


if __name__ == "__main__":
    main()
