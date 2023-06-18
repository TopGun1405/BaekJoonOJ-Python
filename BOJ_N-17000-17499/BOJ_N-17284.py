def main():
    button = {1: 500, 2: 800, 3: 1000}
    money = 5000
    push = list(map(int, input().split()))
    for b in push:
        money -= button[b]
    print(money)


if __name__ == "__main__":
    main()
