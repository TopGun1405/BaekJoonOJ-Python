def main():
    score = [13, 7, 5, 3, 3, 2]
    cho, han = 72, 73.5

    chuk = list(map(int, input().split()))
    eun = list(map(int, input().split()))

    for i in range(6):
        cho += chuk[i] * score[i]
        han += eun[i] * score[i]

    print("cocjr0208" if cho > han else "ekwoo")


if __name__ == "__main__":
    main()
