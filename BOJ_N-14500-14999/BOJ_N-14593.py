def main():
    N = int(input())
    pInfo = [[n] + list(map(int, input().split())) for n in range(1, N + 1)]
    pInfo.sort(key=lambda k: (-k[1], k[2], k[3]))
    print(pInfo[0][0])


if __name__ == "__main__":
    main()
