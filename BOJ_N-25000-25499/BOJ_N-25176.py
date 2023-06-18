def main():
    N = int(input())
    k = 1
    for i in range(1, N + 1):
        k *= i
    print(k)


if __name__ == "__main__":
    main()
