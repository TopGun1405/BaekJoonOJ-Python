def main():
    x = list(input())

    x_min = sorted(x)
    x_max = sorted(x, reverse=True)
    print(str(int("".join(x_max)) - int("".join(x_min))).zfill(len(x)))


if __name__ == "__main__":
    main()
