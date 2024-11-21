def main():
    D = int(input())
    yobi = []
    while True:
        try:
            Y = int(input())
            yobi.append(Y)
        except EOFError:
            break

    for y in yobi:
        if D > y:
            D += y
        else:
            break

    print(D)


if __name__ == "__main__":
    main()
