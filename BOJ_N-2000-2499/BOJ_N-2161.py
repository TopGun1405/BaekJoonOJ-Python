def main():
    N = int(input())
    card = list(range(1, N + 1))

    while True:
        print(card.pop(0), end=' ')
        if not card:
            break
        card.append(card.pop(0))


if __name__ == "__main__":
    main()
