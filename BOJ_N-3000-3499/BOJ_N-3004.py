def main():
    N = int(input())
    print((N // 2 + 1) ** 2 if N % 2 == 0
          else (N // 2 + 1) * (N // 2 + 2))


if __name__ == "__main__":
    main()
