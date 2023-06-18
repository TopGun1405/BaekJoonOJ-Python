def main():
    A, B = map(int, input().split())
    print(1 / (1 + 10 ** ((B - A) / 400)))


if __name__ == "__main__":
    main()
