def main():
    k = int(input())

    if k * 0.01 + 25 < 100:
        print(100)
    elif k * 0.01 + 25 > 2000:
        print(2000)
    else:
        print(k * 0.01 + 25)


if __name__ == "__main__":
    main()
