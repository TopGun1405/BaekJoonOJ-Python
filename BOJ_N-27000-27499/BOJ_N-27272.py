def main():
    a, b, c, d = map(int, input().split())
    print(max(a*b + c*d, a*c + b*d, a*d + b*c))


if __name__ == "__main__":
    main()
