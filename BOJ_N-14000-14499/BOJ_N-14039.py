def main():
    square = [list(map(int, input().split())) for _ in range(4)]

    tot = []
    for i in range(4):
        tot.append(sum(square[i]))
        tot.append(sum([square[j][i] for j in range(4)]))

    print("magic" if len(set(tot)) == 1 else "not magic")


if __name__ == "__main__":
    main()
