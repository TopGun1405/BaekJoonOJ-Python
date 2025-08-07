def main():
    N = int(input())
    HFM = []
    for i in range(1, N+1):
        J_i, P_i = map(int, input().split())
        HFM.append([i, P_i, J_i/P_i])

    HFM.sort(key=lambda k: -k[2])

    print(HFM[0][1] + HFM[1][1] + HFM[2][1])
    print(HFM[0][0])
    print(HFM[1][0])
    print(HFM[2][0])


if __name__ == "__main__":
    main()
