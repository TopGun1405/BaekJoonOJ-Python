def main():
    N = int(input())
    num = sum([N*i+i for i in range(1, N)])
    print(num)


if __name__ == "__main__":
    main()
