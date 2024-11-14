def main():
    N = int(input())
    print("Yes" if N <= 100_000 and N % 2024 == 0 else "No")


if __name__ == "__main__":
    main()
