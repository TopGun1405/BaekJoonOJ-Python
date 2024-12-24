def main():
    N = int(input())
    X = int(input())
    print(f"{(N / (N * (1 - X/100)) - 1) * 100:0.6f}")


if __name__ == "__main__":
    main()
