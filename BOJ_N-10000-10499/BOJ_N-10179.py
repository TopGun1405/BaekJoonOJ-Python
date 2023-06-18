def main():
    t = int(input())
    for _ in range(t):
        n = float(input())
        print("${:0.2f}".format(n * 0.8))


if __name__ == "__main__":
    main()
