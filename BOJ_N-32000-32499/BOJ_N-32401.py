def main():
    N = int(input())
    S = input()

    cnt = 0
    for i in range(N):
        for j in range(i+3, N+1):

            s = S[i:j]
            if s.startswith("A") and s.endswith("A"):
                if s[1:-1].count("A") == 0 and s[1:-1].count("N") == 1:
                    cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
