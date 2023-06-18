def main():
    W = int(input())
    N = int(input())
    k = 0
    for _ in range(N):
        w, l = map(int, input().split())
        k += w * l
    print(k // W)


if __name__ == "__main__":
    main()
