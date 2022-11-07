def main():
    n = int(input())
    for i in range(n):
        data = input()
        print(data)
        if '17' in data and '18' in data:
            print("both")
        elif '17' in data:
            print("zack")
        elif '18' in data:
            print("mack")
        else:
            print("none")
        if i < n - 1:
            print()


if __name__ == "__main__":
    main()
