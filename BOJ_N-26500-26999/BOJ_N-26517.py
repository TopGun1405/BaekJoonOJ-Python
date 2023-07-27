def main():
    k = int(input())
    a, b, c, d = map(int, input().split())
    print(["No", f"Yes {a * k + b}"][a * k + b == c * k + d])


if __name__ == "__main__":
    main()
