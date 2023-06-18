def main():
    t = 1
    while True:
        N = int(input())
        if N == 0:
            break
        birth = {1: "Jan:", 2: "Feb:", 3: "Mar:", 4: "Apr:",
                 5: "May:", 6: "Jun:", 7: "Jul:", 8: "Aug:",
                 9: "Sep:", 10: "Oct:", 11: "Nov:", 12: "Dec:"}
        for _ in range(N):
            d, m, y = map(int, input().split())
            birth[m] += '*'
        print("Case #{}:".format(t))
        print(*birth.values(), sep='\n')
        t += 1


if __name__ == "__main__":
    main()
