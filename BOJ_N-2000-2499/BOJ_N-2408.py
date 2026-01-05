def main():
    N = int(input())
    eq = ""
    for _ in range(2 * N - 1):
        eq += input()
    eq = eq.replace("/", "//")

    print(eval(eq))


if __name__ == "__main__":
    main()
