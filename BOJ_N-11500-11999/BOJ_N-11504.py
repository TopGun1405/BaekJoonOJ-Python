def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        X = int(''.join(input().split()))
        Y = int(''.join(input().split()))
        board_state = list(map(int, input().split()))

        board_state += board_state[:M]
        cnt = 0
        for i in range(N):
            num = int(''.join(map(str, board_state[i:i+M])))
            if X <= num <= Y:
                cnt += 1
        print(cnt)


if __name__ == "__main__":
    main()
