def main():
    n1 = bin(int(input()))[2:][-4:].zfill(4)
    n2 = bin(int(input()))[2:][-4:].zfill(4)
    n3 = bin(int(input()))[2:][-4:].zfill(4)

    print(str(int(n1 + n2 + n3, 2)).zfill(4))


if __name__ == "__main__":
    main()
