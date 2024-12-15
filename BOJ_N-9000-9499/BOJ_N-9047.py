def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        cnt = 0
        while N != 6174:
            cnt += 1
            n = list(str(N))
            N = int("".join(sorted(n, reverse=True))) - int("".join(sorted(n)))

            if N < 1000:
                S = int(str(N) + "0" * (4 - len(str(N))))
                N = int(S)

        print(cnt)


if __name__ == "__main__":
    main()
