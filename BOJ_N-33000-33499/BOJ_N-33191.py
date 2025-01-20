def main():
    b = int(input())
    watermelon = int(input())
    pomegranates = int(input())
    nuts = int(input())

    if b >= watermelon:
        print("Watermelon")
    elif b >= pomegranates:
        print("Pomegranates")
    elif b >= nuts:
        print("Nuts")
    else:
        print("Nothing")


if __name__ == "__main__":
    main()
