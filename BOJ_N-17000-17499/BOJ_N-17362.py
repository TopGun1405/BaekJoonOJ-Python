def main():
    n = int(input())
    print(1 if n % 8 == 1
          else (2 if n % 8 in [0, 2]
                else (3 if n % 8 in [3, 7]
                      else (4 if n % 8 in [4, 6]
                            else 5))))


if __name__ == "__main__":
    main()
