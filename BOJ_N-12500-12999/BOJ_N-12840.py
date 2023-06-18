def main():
    h, m, s = map(int, input().split())
    q = int(input())
    for _ in range(q):
        data = list(map(int, input().split()))
        if len(data) == 1 and data[0] == 3:
            print(h, m, s)
        else:
            t = h * 3600 + m * 60 + s + (data[1] if data[0] == 1 else -data[1])
            if t < 0:
                t += 86400
            t %= 86400
            h, m, s = t // 3600, t % 3600 // 60, t % 60


if __name__ == "__main__":
    main()
