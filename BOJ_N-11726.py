def main():
    n = int(input())
    square = [0, 1, 2]
    for i in range(3, n + 1):
        square.append(square[i - 1] + square[i - 2])
    print(square[n] % 10_007)


if __name__ == "__main__":
    main()
