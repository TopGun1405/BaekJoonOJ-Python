def main():
    N = int(input())
    pos = [[n] + list(map(int, input().split())) for n in range(1, N + 1)]
    maxDis = 0
    cow1, cow2 = 0, 0
    for n1, x1, y1 in pos[:-1]:
        for n2, x2, y2 in pos[n1:]:
            dis = (x2 - x1) ** 2 + (y2 - y1) ** 2
            if dis > maxDis:
                maxDis = dis
                cow1, cow2 = n1, n2
    print(cow1, cow2)


if __name__ == "__main__":
    main()
