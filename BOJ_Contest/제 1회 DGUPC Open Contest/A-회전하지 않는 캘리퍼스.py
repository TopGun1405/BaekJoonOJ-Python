def main():
    N = int(input())
    pos = [list(map(int, input().split())) for _ in range(N)]
    pos.sort(key=lambda k: k[1])
    print(pos[-1][1] - pos[0][1])


if __name__ == "__main__":
    main()
