def main():
    N = int(input()) - 1984
    ten = "0123456789"
    twelve = "ABCDEFGHIJKL"
    print(twelve[N % 12] + ten[N % 10])


if __name__ == "__main__":
    main()
