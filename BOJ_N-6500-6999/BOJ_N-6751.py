def main():
    Y = int(input())
    while True:
        Y += 1
        if len(set(list(str(Y)))) == len(list(str(Y))):
            print(Y)
            break


if __name__ == "__main__":
    main()
