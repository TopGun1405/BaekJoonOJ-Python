def main():
    P = int(input())
    C = int(input())
    print(P * 50 - C * 10 + (500 if P > C else 0))


if __name__ == "__main__":
    main()
