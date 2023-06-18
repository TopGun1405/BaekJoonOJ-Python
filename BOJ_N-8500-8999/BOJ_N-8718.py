def main():
    x, k = map(int, input().split())
    print(k * 7000 if k * 7 <= x
          else (k * 3500 if k * 3.5 <= x
                else (k * 1750 if k * 1.75 <= x
                      else 0)))


if __name__ == "__main__":
    main()
