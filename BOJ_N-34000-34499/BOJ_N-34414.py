def main():
    n = int(input())
    heights = [int(input()) for _ in range(n)]

    print("False" if list(filter(lambda e: e < 48, heights)) else "True")


if __name__ == "__main__":
    main()
