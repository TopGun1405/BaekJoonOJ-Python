def main():
    FizzBuzz = [input() for _ in range(3)]

    for i in range(3):
        if FizzBuzz[i].isdigit():
            n = int(FizzBuzz[i]) + (3 - i)
            if n % 3 == n % 5 == 0:
                print("FizzBuzz")
            elif n % 3 == 0:
                print("Fizz")
            elif n % 5 == 0:
                print("Buzz")
            else:
                print(n)
            break


if __name__ == "__main__":
    main()
