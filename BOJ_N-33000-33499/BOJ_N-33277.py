def main():
    N, M = map(int, input().split())
    K = (M / N) * 24 * 60
    HH = int(K // 60)
    MM = int(K - HH * 60)
    print(f"{HH:02d}:{MM:02d}")


if __name__ == "__main__":
    main()
