def main():
    T = int(input())
    fib = [(1, 0), (0, 1)]
    for i in range(39):
        fib.append((fib[-1][0] + fib[-2][0], fib[-1][1] + fib[-2][1]))
    for _ in range(T):
        N = int(input())
        print(*fib[N])


if __name__ == "__main__":
    main()
