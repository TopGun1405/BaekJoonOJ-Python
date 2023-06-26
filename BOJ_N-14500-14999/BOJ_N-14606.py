def main():
    N = int(input())
    pizza = [0, 0, 1] * 8
    for i in range(3, N + 1):
        j = i // 2
        pizza[i] = j * (i - j) + pizza[j] + pizza[i - j]
    print(pizza[N])

    # print(N * (N - 1) // 2)


if __name__ == "__main__":
    main()
