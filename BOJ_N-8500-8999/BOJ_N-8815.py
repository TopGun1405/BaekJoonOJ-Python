def main():
    Z = int(input())
    for _ in range(Z):
        N = int(input())
        print('A' if N == 1 else "BCBCDCDADABA"[(N - 2) % 12])


if __name__ == "__main__":
    main()
