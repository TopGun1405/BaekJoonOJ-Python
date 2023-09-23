def main():
    N = int(input())
    for _ in range(N):
        Ai, Bi, Xi = map(int, input().split())
        print(Ai * (Xi - 1) + Bi)


if __name__ == "__main__":
    main()
