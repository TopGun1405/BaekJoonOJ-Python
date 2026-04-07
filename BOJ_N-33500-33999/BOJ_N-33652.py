def main():
    N = int(input())
    LED = [list(map(int, input().split())) for _ in range(N)]

    LED.sort(key=lambda k: k[0])
    for i in range(N):
        M, O = LED[i]

        if O == 0:
            print(M)
            break
    else:
        print(-1)


if __name__ == "__main__":
    main()
