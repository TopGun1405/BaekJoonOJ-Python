def main():
    N = int(input())
    for _ in range(N):
        tNum, st, m, sk = map(int, input().split())
        print("{} {} ".format(tNum, st + m + sk), end='')
        pSt, pM, pSk = 35 * 0.3, 25 * 0.3, 40 * 0.3
        print("PASS" if st + m + sk >= 55 and st >= pSt and m >= pM and sk >= pSk
              else "FAIL")


if __name__ == "__main__":
    main()
