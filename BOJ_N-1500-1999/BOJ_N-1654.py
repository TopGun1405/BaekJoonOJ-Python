def main():
    K, N = map(int, input().split())
    cableLen = [int(input()) for _ in range(K)]
    cutCable(cableLen, N)


def cutCable(cableLen, N):
    # 문제 잘 읽어 보기
    # 랜선의 길이는 자연수
    low = 1
    high = max(cableLen)

    while True:
        mid = (low + high) // 2

        if low > high:
            print(mid)
            break

        cable = 0
        for length in cableLen:
            cable += length // mid

        if cable >= N:
            low = mid + 1
        else:
            high = mid - 1


if __name__ == "__main__":
    main()
