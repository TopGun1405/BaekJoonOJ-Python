def main():
    S_ab = int(input())
    F_ab = int(input())

    print("high speed rail" if S_ab <= F_ab else "flight")


if __name__ == "__main__":
    main()
