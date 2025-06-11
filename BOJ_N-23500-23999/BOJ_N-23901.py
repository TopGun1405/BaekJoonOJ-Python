def main():
    T = int(input())
    for x in range(1, T+1):
        N = int(input())
        H = list(map(int, input().split()))

        h = 0
        for i in range(N-2):
            if H[i] < H[i+1] and H[i+1] > H[i+2]:
                h += 1

        print(f"Case #{x}: {h}")


if __name__ == "__main__":
    main()
