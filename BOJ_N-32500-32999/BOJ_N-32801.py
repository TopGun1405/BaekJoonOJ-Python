def main():
    n, a, b = map(int, input().split())

    Fizz, Buzz, FizzBuzz = 0, 0, 0
    for i in range(1, n+1):
        if i % a == 0 and i % b == 0:
            FizzBuzz += 1
        elif i % a == 0:
            Fizz += 1
        elif i % b == 0:
            Buzz += 1
        else:
            continue

    print(Fizz, Buzz, FizzBuzz)


if __name__ == "__main__":
    main()
