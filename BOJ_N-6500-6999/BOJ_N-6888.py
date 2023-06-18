def main():
    X, Y = int(input()), int(input())
    while X <= Y:
        print("All positions change in year {}".format(X))
        X += 60


if __name__ == "__main__":
    main()
