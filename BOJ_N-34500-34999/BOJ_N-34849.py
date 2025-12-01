def main():
    N = int(input())

    print("Accepted" if N ** 2 <= 10 ** 8 else "Time limit exceeded")


if __name__ == "__main__":
    main()
    