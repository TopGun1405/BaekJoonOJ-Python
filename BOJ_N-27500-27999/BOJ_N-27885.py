def main():
    c, h = map(int, input().split())
    times = []
    for _ in range(c + h):
        hh, mm, ss = map(int, input().split(':'))
        times.append(hh*60*60 + mm*60 + ss)
    times.sort()

    prev, tot = -40, 0
    for time in times:
        t = time - prev
        passTime = 40 if t >= 40 else t
        tot += passTime
        prev = time
    print(86400 - tot)


if __name__ == "__main__":
    main()
