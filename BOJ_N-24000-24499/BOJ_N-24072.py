def main():
    A, B, C = map(int, input().split())
    print(1 if A <= C < B else 0)


if __name__ == "__main__":
    main()
