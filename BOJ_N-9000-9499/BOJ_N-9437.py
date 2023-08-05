def main():
    while True:
        try:
            N, P = map(int, input().split())
        except ValueError:
            break
        for k in range(N // 4):
            pages = [2*k+1, 2*k+2, N-2*k-1, N-2*k]
            if P in pages:
                pages.remove(P)
                print(*pages)


if __name__ == "__main__":
    main()
