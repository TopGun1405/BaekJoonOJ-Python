def main():
    N = int(input())
    for _ in range(N):
        A, B = map(lambda s: int(s[::-1]), input().split())
        print(int(str(A + B)[::-1]))


if __name__ == "__main__":
    main()
