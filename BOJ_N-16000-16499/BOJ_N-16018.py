def main():
    N = int(input())
    parking_space = [input() for _ in range(2)]

    cnt = 0
    for i in range(N):
        if parking_space[0][i] + parking_space[1][i] == "CC":
           cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
