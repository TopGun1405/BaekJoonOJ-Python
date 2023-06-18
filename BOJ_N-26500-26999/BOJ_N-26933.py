def main():
    N = int(input())
    need = 0
    for _ in range(N):
        H, B, K = map(int, input().split())
        need = need + (0 if H >= B else (B - H) * K)
    print(need)


if __name__ == "__main__":
    main()
