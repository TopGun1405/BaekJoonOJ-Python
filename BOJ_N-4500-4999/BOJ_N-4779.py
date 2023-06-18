def main():

    def dashRecursion(idx, n):
        d = n // 3
        if d == 0:
            return

        for i in range(d, d * 2):
            arr[idx + i] = ' '

        dashRecursion(idx, d)
        dashRecursion(idx + d * 2, d)

    while True:
        try:
            N = 3 ** int(input())
            arr = ['-' for _ in range(N)]
            dashRecursion(0, N)
            print(''.join(arr))
        except EOFError:
            break


if __name__ == "__main__":
    main()
