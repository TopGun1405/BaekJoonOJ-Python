def main():
    T = int(input())
    for t in range(1, T + 1):
        H, M = map(int, input().split())
        if M < 45:
            M, H = M + 15, H - 1
        else:
            M -= 45
        if H == -1:
            H += 24
        print("Case #{}: {} {}".format(t, H, M))


if __name__ == "__main__":
    main()
