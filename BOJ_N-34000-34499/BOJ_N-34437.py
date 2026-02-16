def main():
    N = int(input())

    step = 0
    while N != 1:
        if N % 2 == 0:
            N //= 2
        else:
            N = N + (N * 2 + 1)
        step += 1

    print(step)


if __name__ == "__main__":
    main()
