def main():
    N = int(input())

    if N % 2 == 0:
        print("I LOVE CBNU")
    else:
        k = N // 2
        print("*" * N)
        for i in range(k + 1):
            if i == 0:
                print(" " * k + "*")
            else:
                print(" " * (k-i) + "*" + " " * (2*i-1) + "*")


if __name__ == "__main__":
    main()
