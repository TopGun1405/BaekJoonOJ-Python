def main():
    n = int(input())
    print(0 if n % 2 == 1
          else (2 if n // 2 % 2 == 0
                else 1))


if __name__ == "__main__":
    main()
