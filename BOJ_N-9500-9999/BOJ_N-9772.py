def main():
    while True:
        x, y = map(float, input().split())
        if x == y == 0:
            print("AXIS")
            break
        print("AXIS" if x == 0 or y == 0
              else ("Q1" if x > 0 and y > 0
                    else ("Q2" if x < 0 < y
                          else ("Q3" if x < 0 and y < 0
                                else "Q4"))))


if __name__ == "__main__":
    main()
