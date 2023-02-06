def main():
    N = int(input())
    fact = 1
    for n in range(1, N + 1):
        fact *= n
    print(fact)


if __name__ == "__main__":
    main()
