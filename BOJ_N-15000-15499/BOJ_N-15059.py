def main():
    Ca, Ba, Pa = map(int, input().split())
    Cr, Br, Pr = map(int, input().split())

    tot = 0
    if Cr > Ca:
        tot += Cr - Ca
    if Br > Ba:
        tot += Br - Ba
    if Pr > Pa:
        tot += Pr - Pa
    print(tot)


if __name__ == "__main__":
    main()
