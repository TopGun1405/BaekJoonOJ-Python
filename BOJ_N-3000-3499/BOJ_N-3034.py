def main():
    N, W, H = map(int, input().split())
    for _ in range(N):
        s = int(input())
        print("DA" if s <= W or s <= H or s <= (W * W + H * H) ** 0.5 else "NE")


if __name__ == "__main__":
    main()
