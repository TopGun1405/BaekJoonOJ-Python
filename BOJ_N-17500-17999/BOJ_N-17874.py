def main():
    n, h, v = map(int, input().split())
    cake = [h * v, h * (n - v), (n - h) * v, (n - h) * (n - v)]
    print(max(cake) * 4)


if __name__ == "__main__":
    main()
