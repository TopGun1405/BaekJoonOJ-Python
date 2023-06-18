def main():
    num = int(input())
    car = list(map(int, input().split()))

    print(car.count(num))


if __name__ == "__main__":
    main()
