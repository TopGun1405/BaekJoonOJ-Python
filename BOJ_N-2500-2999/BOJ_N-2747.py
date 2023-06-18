def main():
    n = int(input())
    fib = [0, 1]
    for i in range(n - 1):
        fib.append(fib[-1] + fib[-2])
    print(fib[-1])


if __name__ == "__main__":
    main()
