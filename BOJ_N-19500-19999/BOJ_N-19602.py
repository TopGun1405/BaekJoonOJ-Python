def main():
    S, M, L = int(input()), int(input()), int(input())
    print("sad" if S + 2 * M + 3 * L < 10 else "happy")


if __name__ == "__main__":
    main()
