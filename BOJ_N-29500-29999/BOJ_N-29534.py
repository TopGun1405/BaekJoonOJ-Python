def main():
    n = int(input())
    s = input()

    if len(s) > n:
        print("Impossible")
    else:
        cube = 0
        for c in s:
            cube += ord(c) - 96

        print(cube)


if __name__ == "__main__":
    main()
