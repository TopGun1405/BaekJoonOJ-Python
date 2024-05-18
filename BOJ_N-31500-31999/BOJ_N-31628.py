def main():
    eggplants = [input().split() for _ in range(10)]

    for i in range(10):
        row = set(eggplants[i])
        col = set([eggplants[j][i] for j in range(10)])
        if len(row) == 1 or len(col) == 1:
            print(1)
            break
    else:
        print(0)


if __name__ == "__main__":
    main()
