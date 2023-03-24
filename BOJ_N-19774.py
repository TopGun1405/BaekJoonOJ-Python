def main():
    t = int(input())
    for _ in range(t):
        i = int(input())
        x, y = i // 100, i % 100
        print("YES" if (x ** 2 + y ** 2) % 7 == 1 else "NO")


if __name__ == "__main__":
    main()
