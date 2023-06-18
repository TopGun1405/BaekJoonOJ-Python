def main():
    n, m = map(int, input().split())
    print(["NO", "YES"][(n * m) % 3 == 0])


if __name__ == "__main__":
    main()
