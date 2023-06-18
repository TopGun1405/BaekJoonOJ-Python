def main():
    sPrice, sWeight = map(int, input().split())
    nPrice, nWeight = map(int, input().split())
    uPrice, uWeight = map(int, input().split())
    S = (sWeight * 10) / ((sPrice * 10 - 500) if sPrice * 10 >= 5000 else (sPrice * 10))
    N = (nWeight * 10) / ((nPrice * 10 - 500) if nPrice * 10 >= 5000 else (nPrice * 10))
    U = (uWeight * 10) / ((uPrice * 10 - 500) if uPrice * 10 >= 5000 else (uPrice * 10))
    print('S' if S > N and S > U
          else ('N' if N > S and N > U
                else 'U'))


if __name__ == "__main__":
    main()
