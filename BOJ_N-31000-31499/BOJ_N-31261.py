def main():
    a, b = map(int, input().split())
    # (x / a - a) / a - a = b
    print((((b + a) * a) + a) * a)


if __name__ == "__main__":
    main()
