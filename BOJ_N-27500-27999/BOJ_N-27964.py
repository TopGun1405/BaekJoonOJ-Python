def main():
    N = int(input())
    toppings = input().split()

    cheese = set()
    for topping in toppings:
        if len(topping) >= 6 and topping[-6:] == "Cheese":
            cheese.add(topping)

    print("yummy" if len(cheese) >= 4 else "sad")


if __name__ == "__main__":
    main()
