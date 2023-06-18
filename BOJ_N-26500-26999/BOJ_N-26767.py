def main():
    N = int(input())
    for n in range(1, N + 1):
        if n % 7 == 0 and n % 11 == 0:
            print("Wiwat!")
        elif n % 7 == 0:
            print("Hurra!")
        elif n % 11 == 0:
            print("Super!")
        else:
            print(n)


if __name__ == "__main__":
    main()
