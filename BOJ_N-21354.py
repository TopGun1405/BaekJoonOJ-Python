def main():
    A, P = map(int, input().split())
    print("Axel" if A * 7 > P * 13
          else ("Petra" if A * 7 < P * 13
                else "lika"))


if __name__ == "__main__":
    main()
