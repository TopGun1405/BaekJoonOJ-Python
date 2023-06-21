def main():
    N, H, W = map(int, input().split())
    text = ['?'] * N
    for _ in range(H):
        s = input()
        for i in range(N * W):
            if s[i] != '?':
                text[i // W] = s[i]
    print(''.join(text))


if __name__ == "__main__":
    main()
