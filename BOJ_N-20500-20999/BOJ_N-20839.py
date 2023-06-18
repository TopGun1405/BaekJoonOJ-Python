def main():
    x, y, z = map(int, input().split())
    x1, y1, z1 = map(int, input().split())
    print('A' if x1 == x and y1 == y and z1 == z
          else ('B' if x1 >= x / 2 and y1 == y and z1 == z
                else ('C' if y1 == y and z1 == z
                      else ('D' if y1 >= y / 2 and z1 == z
                            else 'E'))))


if __name__ == "__main__":
    main()
