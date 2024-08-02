def main():
    n, m, k, a, b, c = map(int, input().split())

    army = [["Joffrey", n*a], ["Robb", m*b], ["Stannis", k*c]]
    army.sort(key=lambda key: key[1], reverse=True)
    names = list(map(lambda e: e[0], filter(lambda e: e[1] == army[0][1], army)))

    print(*sorted(names))


if __name__ == "__main__":
    main()
