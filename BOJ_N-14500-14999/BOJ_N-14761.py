def main():
    X, Y, N = map(int, input().split())
    for i in range(1, N + 1):
        if i % X == i % Y == 0:
            print("FizzBuzz")
        elif i % X == 0:
            print("Fizz")
        elif i % Y == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    main()
