def main():
    x, y = map(int, input().split())
    exceptFoo = 100 - x
    print(x / (exceptFoo * (y / (100 - y))))


if __name__ == "__main__":
    main()
