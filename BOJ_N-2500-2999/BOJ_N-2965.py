def main():
    A, B, C = map(int, input().split())
    print(max(B - A, C - B) - 1)


if __name__ == "__main__":
    main()
