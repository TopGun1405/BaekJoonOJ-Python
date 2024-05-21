def main():
    N = int(input())
    info = [
        list(map(lambda e: int(e) if e.isdigit() else e, input().split())) for _ in range(N)
    ]
    info.sort(key=lambda k: (-k[1], k[2], -k[3], k[0]))
    print(*list(map(lambda e: e[0], info)), sep="\n")


if __name__ == "__main__":
    main()
