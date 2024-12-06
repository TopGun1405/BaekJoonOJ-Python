def main():
    k = int(input())

    c = 2**k - 1
    print(bin(c * (c + 1) // 2)[2:])


if __name__ == "__main__":
    main()
