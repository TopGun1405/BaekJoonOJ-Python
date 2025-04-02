def main():
    d = list(map(int, input().split()))
    n = [[1], [5], [10], [20], [50], [100]]

    maxVal = 0
    for i in range(6):
        n[i].append(n[i][0] * d[i])
        n[i].append(d[i])
        maxVal = max(maxVal, n[i][1])

    n = list(filter(lambda k: k[1] == maxVal, n))
    n.sort(key=lambda k: k[2])

    print(n[0][0])


if __name__ == "__main__":
    main()
