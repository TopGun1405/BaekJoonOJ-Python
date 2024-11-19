def main():
    way = [int(input()) for _ in range(3)]
    print("JAH" if way[0] in [1, 3] and way[1] in [6, 8] and way[2] in [2, 5] else "EI")


if __name__ == "__main__":
    main()
