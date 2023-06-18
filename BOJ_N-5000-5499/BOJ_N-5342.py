def main():
    items = {"Paper": 57.99, "Printer": 120.50, "Planners": 31.25,
             "Binders": 22.50, "Calendar": 10.95, "Notebooks": 11.20, "Ink": 66.95}
    dollar = 0
    while True:
        name = input()
        if name == "EOI":
            break
        dollar += items[name]
    print(f"${dollar}")


if __name__ == "__main__":
    main()
