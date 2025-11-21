def main():
    m, d = map(int, input().split())

    print(d // m + (1 if d / m != d // m else 0))


if __name__ == "__main__":
    main()
