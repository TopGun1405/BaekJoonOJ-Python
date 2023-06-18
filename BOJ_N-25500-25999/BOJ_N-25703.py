def main():
    N = int(input())
    print("int a;")
    for n in range(1, N + 1):
        if n == 1:
            print("int *ptr = &a;")
        elif n == 2:
            print("int {}ptr{} = &ptr;".format('*' * n, n))
        else:
            print("int {}ptr{} = &ptr{};".format('*' * n, n, n - 1))


if __name__ == "__main__":
    main()
