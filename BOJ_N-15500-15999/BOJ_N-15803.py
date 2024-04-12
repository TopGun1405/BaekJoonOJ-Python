def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    k1 = (y2 - y1) / (x2 - x1) if x2 != x1 else int(1e9)
    k2 = (y3 - y2) / (x3 - x2) if x3 != x2 else int(1e9)

    print("WHERE IS MY CHICKEN?"if k1 == k2
          else "WINNER WINNER CHICKEN DINNER!")


if __name__ == "__main__":
    main()
