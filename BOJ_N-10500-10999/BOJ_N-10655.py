def main():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]

    maxVal = 0
    for i in range(1, N-1):
        x_i, y_i = points[i][0], points[i][1]
        x_j, y_j = points[i+1][0], points[i+1][1]
        x_k, y_k = points[i-1][0], points[i-1][1]

        curr = abs(x_i - x_j) + abs(y_i - y_j)
        prev = abs(x_k - x_i) + abs(y_k - y_i)
        vals = curr + prev - (abs(x_j - x_k) + abs(y_j - y_k))

        maxVal = max(vals, maxVal)

    totVal = 0
    for i in range(1, N):
        totVal += abs(points[i-1][0] - points[i][0]) + abs(points[i-1][1] - points[i][1])

    print(totVal - maxVal)


if __name__ == "__main__":
    main()
