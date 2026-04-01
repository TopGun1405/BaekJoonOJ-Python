def main():
    T = int(input())
    for _ in range(T):
        N, S = map(int, input().split())

        print("Yes" if S == 10**7 + N else "No")


if __name__ == "__main__":
    main()
