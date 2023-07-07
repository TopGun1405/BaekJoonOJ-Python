def main():
    t = int(input())
    for _ in range(t):
        w, n = input().split()
        n = int(n)
        print(f"Shifting {w} by {n} positions gives us: {w[-n:] + w[:len(w)-n]}")


if __name__ == "__main__":
    main()
