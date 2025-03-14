def main():
    N = int(input())
    price = [float(input()) for _ in range(N)]

    print(f"{sorted(price)[1]:.02f}")


if __name__ == "__main__":
    main()
