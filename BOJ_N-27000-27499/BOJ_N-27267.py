def main():
    a, b, c, d = map(int, input().split())
    print("M" if a * b > c * d else ("P" if a * b < c * d else "E"))


if __name__ == "__main__":
    main()
