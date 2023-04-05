def main():
    N = int(input())
    for _ in range(N):
        P, C = map(float, input().split())
        print(100 * P / (100 + C))


if __name__ == "__main__":
    main()
