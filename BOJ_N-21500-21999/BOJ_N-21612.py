def main():
    B = int(input())
    P = 5 * B - 400
    print(P)
    print(1 if P < 100 else (-1 if P > 100 else 0))


if __name__ == "__main__":
    main()
