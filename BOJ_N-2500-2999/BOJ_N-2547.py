def main():
    T = int(input())
    for _ in range(T):
        input()
        N = int(input())
        candy = 0
        for _ in range(N):
            candy += int(input())
        print("YES" if candy % N == 0 else "NO")


if __name__ == "__main__":
    main()
