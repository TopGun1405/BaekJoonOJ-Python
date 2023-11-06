def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        C = list(map(int, input().split()))
        cnt = 0
        while True:
            C = [c if c % 2 == 0 else c + 1 for c in C]
            if len(set(C)) == 1:
                print(cnt)
                break
            C = [(C[i] + C[(i + 1) % N]) // 2 for i in range(N)]
            cnt += 1


if __name__ == "__main__":
    main()
