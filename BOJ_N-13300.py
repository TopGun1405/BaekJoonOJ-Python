def main():
    N, K = map(int, input().split())
    students = {y: {0: 0, 1: 0} for y in range(1, 7)}
    for _ in range(N):
        S, Y = map(int, input().split())
        students[Y][S] += 1
    room = 0
    for y in students:
        g, b = students[y][0], students[y][1]
        room = room + g // K + (1 if g % K else 0)
        room = room + b // K + (1 if b % K else 0)
    print(room)


if __name__ == "__main__":
    main()
