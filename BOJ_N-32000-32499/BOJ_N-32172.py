def main():
    N = int(input())

    A, A_i = {0}, 0
    for i in range(1, N+1):
        if A_i - i < 0 or A_i - i in A:
            A_i += i
        else:
            A_i -= i
        A.add(A_i)

    print(A_i)


if __name__ == "__main__":
    main()
