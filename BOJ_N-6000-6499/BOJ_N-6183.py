def main():
    N, M = map(int, input().split())
    names = [input().lower() for _ in range(N)]
    goodStr = [input().lower() for _ in range(M)]
    for name in names:
        points = 0
        for s in goodStr:
            i = 0
            for c in name:
                if i == len(s):
                    break
                if s[i] == c:
                    i += 1
            print('i', i)
            if i == len(s):
                points += 1
        print(points)


if __name__ == "__main__":
    main()
