def main():
    Z = int(input())
    for _ in range(Z):
        W, K = map(int, input().split())
        print(W * K // 2)


if __name__ == "__main__":
    main()
    