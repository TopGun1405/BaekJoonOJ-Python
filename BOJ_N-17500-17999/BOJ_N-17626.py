def main():
    n = int(input())
    squares = [0] + [50_001 for _ in range(n)]

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            k = j ** 2
            if k > i:
                break
            squares[i] = min(squares[i], squares[i-k] + 1)

    # print(squares)
    print(squares[n])


if __name__ == "__main__":
    main()
