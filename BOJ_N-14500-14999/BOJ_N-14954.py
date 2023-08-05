def main():
    n = int(input())
    while True:
        n = sum(map(lambda e: int(e)**2, list(str(n))))
        if n == 4:
            print("UNHAPPY")
            break
        elif n == 1:
            print("HAPPY")
            break


if __name__ == "__main__":
    main()
