def main():
    price = [int(input()) for _ in range(5)]
    set_p = [price[i] + price[3 + j] - 50 for i in range(3) for j in range(2)]
    print(min(set_p))


if __name__ == "__main__":
    main()
