def main():
    c1, c2 = map(int, input().split())
    print(c1 if c1 == c2 else (c1 if c1 > c2 else c2))


if __name__ == "__main__":
    main()
