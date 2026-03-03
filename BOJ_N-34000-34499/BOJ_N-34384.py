from math import ceil


def main():
    sec = int(input())

    remain = 3600 - (sec % 3600)

    print(ceil(remain / 60))


if __name__ == "__main__":
    main()
