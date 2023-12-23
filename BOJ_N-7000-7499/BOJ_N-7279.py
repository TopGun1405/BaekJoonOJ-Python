def main():
    N, K = map(int, input().split())
    sit, stand = 0, 0
    for _ in range(N):
        ai, bi = map(int, input().split())
        sit += ai - bi
        stand = max(stand, sit - K)
    print(stand)


if __name__ == "__main__":
    main()
