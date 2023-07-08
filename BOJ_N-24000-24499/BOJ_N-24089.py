def main():
    N, M = map(int, input().split())
    box = {n: n for n in range(1, N + 1)}
    for _ in range(M):
        Xj, Yj = map(int, input().split())
        box[Xj] = Yj
    print(*box.values(), sep='\n')


if __name__ == "__main__":
    main()
