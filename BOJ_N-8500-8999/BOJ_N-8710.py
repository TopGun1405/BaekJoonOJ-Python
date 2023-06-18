def main():
    k, w, m = map(int, input().split())
    print((w - k) // m if (w - k) % m == 0 else (w - k) // m + 1)


if __name__ == "__main__":
    main()
