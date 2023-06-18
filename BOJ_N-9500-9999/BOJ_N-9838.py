def main():
    n = int(input())
    gifts = [int(input()) for _ in range(n)]
    chk = dict()
    for idx, gift in enumerate(gifts, start=1):
        chk[gift] = idx
    items = [item[1] for item in sorted(chk.items(), key=lambda k: k[0])]
    for i in items:
        print(i)


if __name__ == "__main__":
    main()
