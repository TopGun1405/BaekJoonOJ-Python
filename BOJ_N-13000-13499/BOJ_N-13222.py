def main():
    N, W, H = map(int, input().split())
    for _ in range(N):
        M = int(input())
        print("YES" if M <= W or M <= H or M <= (W**2 + H**2)**0.5 else "NO")


if __name__ == "__main__":
    main()
