def main():
    N, M = map(int, input().split())
    inputs = [list(map(lambda e: int(e) if e.isdigit() else e, input().split())) for _ in range(M)]
    inputs.sort(key=lambda k: (k[1], k[0]))
    # [print(inputs[i][2], end='') for i in range(M)]
    print(*map(lambda e: e[2], inputs), sep='')


if __name__ == "__main__":
    main()
