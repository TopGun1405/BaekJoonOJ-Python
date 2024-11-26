def main():
    N = int(input())
    if N == 1:
        print(1)
    else:
        for i in range(2, 10):
            if N % i == 0 and N // i < 10:
                print(1)
                break
        else:
            print(0)


if __name__ == "__main__":
    main()
