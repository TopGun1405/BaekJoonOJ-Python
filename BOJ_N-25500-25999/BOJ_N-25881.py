def main():
    a, b = map(int, input().split())
    n = int(input())
    for _ in range(n):
        kwh = int(input())
        print(kwh, 1000 * a + (kwh - 1000) * b if kwh > 1000 else kwh * a)


if __name__ == "__main__":
    main()
