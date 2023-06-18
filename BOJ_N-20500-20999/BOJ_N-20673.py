def main():
    p, q = int(input()), int(input())
    print("White" if p <= 50 and q <= 10 else ("Red" if q > 30 else "Yellow"))


if __name__ == "__main__":
    main()
