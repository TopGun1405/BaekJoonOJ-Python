def main():
    T, S = map(int, input().split())
    print(320 if 12 <= T <= 16 and S == 0 else 280)


if __name__ == "__main__":
    main()
