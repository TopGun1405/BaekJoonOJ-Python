def main():
    N = int(input())
    Y = [list(input()) for _ in range(N)]

    cnt = [[i+1, [Y[j][i] for j in range(N)].count("Y")] for i in range(len(Y[0]))]
    cnt.sort(key=lambda k: k[1], reverse=True)
    cnt = list(map(lambda e: e[0], filter(lambda e: e[1] == cnt[0][1], cnt)))

    print(",".join(map(str, cnt)))


if __name__ == "__main__":
    main()
