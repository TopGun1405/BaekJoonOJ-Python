def main():
    T = int(input())
    for _ in range(T):
        N = input()
        num = str(int(N) + int(N[::-1]))
        print("YES" if num == num[::-1] else "NO")


if __name__ == "__main__":
    main()
