def main():
    i = 1
    while True:
        num = list(map(int, input().split()))
        if num[0] == 0:
            break
        num[1:].sort()
        print("Case {}: Sorting... done!".format(i))
        i += 1


if __name__ == "__main__":
    main()
