def main():
    N = int(input())
    l = set(int(input()) for _ in range(N))
    s = set(range(1, 6))

    print("YES" if s - l else "NO")


if __name__ == "__main__":
    main()
