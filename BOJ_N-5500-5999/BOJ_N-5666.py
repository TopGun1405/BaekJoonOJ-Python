def main():
    while True:
        try:
            H, P = map(int, input().split())
            print("{:0.2f}".format(H / P))
        except EOFError:
            break


if __name__ == "__main__":
    main()
