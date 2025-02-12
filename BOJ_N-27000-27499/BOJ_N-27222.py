def main():
    n = int(input())
    train = list(map(int, input().split()))

    muscle = 0
    for i in range(n):
        x_i, y_i = map(int, input().split())
        if train[i] and y_i > x_i:
            muscle += y_i - x_i

    print(muscle)


if __name__ == "__main__":
    main()
