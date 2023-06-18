def main():
    T = int(input())
    for _ in range(T):
        N, C = map(int, input().split())
        print(N // C if N % C == 0 else N // C + 1)


if __name__ == "__main__":
    main()
