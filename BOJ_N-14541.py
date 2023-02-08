def main():
    while True:
        n = int(input())
        if n == -1:
            break
        s, t = map(int, input().split())
        m = s * t
        for _ in range(n - 1):
            ss, tt = map(int, input().split())
            m, t = m + ss * (tt - t), tt
        print(m, "miles")


if __name__ == "__main__":
    main()
