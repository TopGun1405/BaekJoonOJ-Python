def main():
    birth = list(map(int, input().split()))
    day = list(map(int, input().split()))

    print(0 if day[0] == birth[0]
          else (day[0] - birth[0]
                if day[1] > birth[1]
                else (day[0] - birth[0]
                      if day[1] == birth[1] and day[2] >= birth[2]
                      else day[0] - birth[0] - 1)))
    print(day[0] - birth[0] + 1)
    print(day[0] - birth[0])


if __name__ == "__main__":
    main()
