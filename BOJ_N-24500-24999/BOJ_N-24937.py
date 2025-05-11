def main():
    N = int(input())
    S = "SciComLove"
    print(S[N % 10:] + S[:N % 10])


if __name__ == "__main__":
    main()
