def main():
    p = [int(input()) for _ in range(4)]
    print("ignore" if (p[0] == 8 or p[0] == 9) and p[1] == p[2] and (p[3] == 8 or p[3] == 9)
          else "answer")


if __name__ == "__main__":
    main()
