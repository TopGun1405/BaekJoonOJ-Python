def main():
    W, N, P = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    for h in H:
        if W <= h <= N:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
