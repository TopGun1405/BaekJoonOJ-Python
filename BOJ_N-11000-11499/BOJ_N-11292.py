def main():
    while True:
        N = int(input())
        if N == 0:
            break
        info = [input().split() for _ in range(N)]
        # info = []
        # for _ in range(N):
        #     name, height = input().split()
        #     info.append([name, int(height)])
        info.sort(key=lambda k: k[1], reverse=True)
        print(*map(lambda e: e[0], filter(lambda e: e[1] == info[0][1], info)))


if __name__ == "__main__":
    main()
