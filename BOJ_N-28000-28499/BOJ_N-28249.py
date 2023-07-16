def main():
    Peppers = {
        "Poblano": 1500,
        "Mirasol": 6000,
        "Serrano": 15500,
        "Cayenne": 40000,
        "Thai": 75000,
        "Habanero": 125000
    }

    N = int(input())
    T = 0
    for _ in range(N):
        name = input()
        T += Peppers[name]
    print(T)


if __name__ == "__main__":
    main()
