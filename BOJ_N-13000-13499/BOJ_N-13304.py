from math import ceil


def main():
    N, K = map(int, input().split())

    STD = [0, 0, 0, 0, 0]
    for _ in range(N):
        S, Y = map(int, input().split())
        if Y == 1 or Y == 2:
            STD[0] += 1
        elif S == 0 and (Y == 3 or Y == 4):
            STD[1] += 1
        elif S == 1 and (Y == 3 or Y == 4):
            STD[2] += 1
        elif S == 0 and (Y == 5 or Y == 6):
            STD[3] += 1
        else:
            STD[4] += 1

    rooms = 0
    for S_i in STD:
        rooms += ceil(S_i / K)
    print(rooms)


if __name__ == "__main__":
    main()
