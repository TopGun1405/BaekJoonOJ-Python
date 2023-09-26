def main():
    hh = int(input())
    alarm = int(input())
    print(alarm + (24 if 20 <= hh < 24 else 0) - hh)


if __name__ == "__main__":
    main()
