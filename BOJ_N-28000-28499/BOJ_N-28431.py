def main():
    socks = [input() for _ in range(5)]
    print(list(filter(lambda e: socks.count(e) % 2 == 1, socks))[0])


if __name__ == "__main__":
    main()
