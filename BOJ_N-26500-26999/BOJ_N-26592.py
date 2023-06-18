def main():
    n = int(input())
    for _ in range(n):
        area, base = map(float, input().split())
        print("The height of the triangle is {:0.2f} units".format(area / base * 2))


if __name__ == "__main__":
    main()
