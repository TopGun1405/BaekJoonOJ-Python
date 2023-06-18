def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        scr, tot = 0, 0
        for _ in range(N):
            s, g = map(float, input().split())
            tot += s * g
            scr += s
        print(int(scr), tot / scr)


if __name__ == "__main__":
    main()
