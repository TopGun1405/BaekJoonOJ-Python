def main():
    lt = set(list(input()))
    print(*({chr(n) for n in range(65, 91)} - lt))


if __name__ == "__main__":
    main()
