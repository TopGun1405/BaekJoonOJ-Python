def main():
    N = int(input())
    print(int(bin(N)[2:][::-1], 2))


if __name__ == "__main__":
    main()
