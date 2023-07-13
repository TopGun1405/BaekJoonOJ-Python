def main():
    N, K = map(int, input().split())
    pixels = [list(map(lambda c: ' '.join(c*K), input().split())) for _ in range(N)]
    for pixel in pixels:
        for _ in range(K):
            print(*pixel)


if __name__ == "__main__":
    main()
