def main():
    cnt = 1
    while True:
        N = int(input())

        if N == 0:
            break

        menu, minVal = 0, 1e9
        for _ in range(N):
            D, P = map(int, input().split())
            if minVal > P / D**2:
                menu = D
                minVal = P / D**2

        print(f"Menu {cnt}: {menu}")
        cnt += 1


if __name__ == "__main__":
    main()
