def main():
    t = int(input())
    for _ in range(t):
        a = input()
        b = input()

        print("YES" if set(b) <= set(a) else "NO")


if __name__ == "__main__":
    main()
