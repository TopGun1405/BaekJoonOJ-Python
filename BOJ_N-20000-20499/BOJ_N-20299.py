def main():
    N, K, L = map(int, input().split())
    VIP = []
    for _ in range(N):
        x1, x2, x3 = map(int, input().split())
        if x1 >= L and x2 >= L and x3 >= L and x1 + x2 + x3 >= K:
            VIP.append([x1, x2, x3])

    print(len(VIP))
    for vip in VIP:
        print(*vip, end=" ")


if __name__ == "__main__":
    main()
