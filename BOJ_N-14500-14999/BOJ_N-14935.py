def main():
    x = list(input())
    while True:
        f = int(x[0]) * len(x)
        if f == int(''.join(x)):
            print("FA")
            break
        x = list(str(f))


if __name__ == "__main__":
    main()
