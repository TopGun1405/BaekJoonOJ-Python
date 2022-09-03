def main():
    a, b = input().split()
    print(bin(int(a, 2) + int(b, 2))[2:])


if __name__ == "__main__":
    main()
