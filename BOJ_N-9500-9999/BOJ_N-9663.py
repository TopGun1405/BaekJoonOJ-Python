def main():
    N = int(input())
    vertical = [1] * N
    diagonal = [1] * (2 * N - 1)
    reverse_d = [1] * (2 * N - 1)
    print(queen(0, N, vertical, diagonal, reverse_d))


def queen(y, n, v, d, r):
    if y == n:
        return 1
    case = 0
    for x in range(n):
        if v[x] and d[y + x] and r[y - x]:
            # print(x, y)
            v[x] = d[y + x] = r[y - x] = 0
            case += queen(y + 1, n, v, d, r)
            v[x] = d[y + x] = r[y - x] = 1
    return case


if __name__ == "__main__":
    main()
