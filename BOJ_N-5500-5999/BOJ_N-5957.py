def main():
    N = int(input())

    dishes = [n for n in range(N, 0, -1)]
    washing, drying = [], []

    while True:
        C_i, D_i = map(int, input().split())
        for _ in range(D_i):
            if C_i == 1:
                washing.append(dishes.pop())
            else:
                drying.append(washing.pop())

        if len(drying) == N:
            break

    print(*drying[::-1], sep="\n")


if __name__ == "__main__":
    main()
