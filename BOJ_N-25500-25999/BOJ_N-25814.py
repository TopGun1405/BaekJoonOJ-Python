def main():
    a, b = input().split()
    wa, wb = len(a) * sum(map(int, a)), len(b) * sum(map(int, b))
    print(1 if wa > wb else (2 if wa < wb else 0))


if __name__ == "__main__":
    main()
