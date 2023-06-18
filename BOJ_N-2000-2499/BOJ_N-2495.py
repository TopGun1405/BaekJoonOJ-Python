def main():
    for _ in range(3):
        N = input()
        mx, cnt = 1, 1
        for i in range(1, 8):
            if N[i] == N[i - 1]:
                cnt += 1
            else:
                mx, cnt = max(cnt, mx), 1
        print(max(cnt, mx))


if __name__ == "__main__":
    main()
