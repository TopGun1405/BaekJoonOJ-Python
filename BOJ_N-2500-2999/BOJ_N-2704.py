def main():
    N = int(input())
    for _ in range(N):
        H, M, S = map(lambda c: bin(int(c))[2:].rjust(6, "0"), input().split(":"))

        col = "".join([h+m+s for h, m, s in zip(H, M, S)])
        row = H + M + S

        print(f"{col} {row}")


if __name__ == "__main__":
    main()
