def main():
    R, C, ZR, ZC = map(int, input().split())
    news = [list(input()) for _ in range(R)]
    for s in news:
        for _ in range(ZR):
            print(''.join(map(lambda c: c * ZC, s)))


if __name__ == "__main__":
    main()
