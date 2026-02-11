def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        timeline = [0] * 1_001
        for _ in range(n):
            c, a, b = map(lambda e: int(e) if e.isdigit() else e, input().split())
            for time in range(a, b):
                timeline[time] += 1

        res = []
        for time in range(1_001):
            if timeline[time] > 0:
                i = timeline[time]
                res.append(chr(ord("A") + i - 1))

        print("".join(res))


if __name__ == "__main__":
    main()
