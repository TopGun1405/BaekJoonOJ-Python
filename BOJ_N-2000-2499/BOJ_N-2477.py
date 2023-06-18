def main():
    K = int(input())

    field_f = dict()
    field = []
    for _ in range(6):
        w, d = map(int, input().split())
        if w not in field_f:
            field_f.update({w: [d]})
        else:
            field_f[w].append(d)
        field.append([w, d])
    blank = []

    # needs improving
    for i in range(6):
        a, b, c = i % 6, (i + 1) % 6, (i + 2) % 6
        if field[a][0] == 3 and field[b][0] == 1 and field[c][0] == 3:
            blank.append(field[b])
            blank.append(field[c])
        elif field[a][0] == 1 and field[b][0] == 4 and field[c][0] == 1:
            blank.append(field[b])
            blank.append(field[c])
        elif field[a][0] == 4 and field[b][0] == 2 and field[c][0] == 4:
            blank.append(field[b])
            blank.append(field[c])
        elif field[a][0] == 2 and field[b][0] == 3 and field[c][0] == 2:
            blank.append(field[b])
            blank.append(field[c])

    print(field_f)
    print(field)
    print(blank)
    big = sum(field_f[blank[0][0]]) * sum(field_f[blank[1][0]])
    small = blank[0][1] * blank[1][1]
    print((big - small) * K)


if __name__ == "__main__":
    main()
