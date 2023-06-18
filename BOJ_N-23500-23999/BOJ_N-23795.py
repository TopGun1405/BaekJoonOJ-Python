def main():
    money = 0
    while True:
        m = int(input())
        if m == -1:
            print(money)
            break
        money += m


if __name__ == "__main__":
    main()
