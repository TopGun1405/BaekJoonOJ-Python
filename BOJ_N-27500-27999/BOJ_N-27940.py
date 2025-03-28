def main():
    N, M, K = map(int, input().split())
    floors = [list(map(int, input().split())) for _ in range(M)]

    F1 = 0
    for i in range(1, M + 1):
        t_i, r_i = floors[i - 1]

        F1 += r_i
        if F1 > K:
            print(f"{i} {1}")
            break
    else:
        print(-1)


if __name__ == "__main__":
    main()
