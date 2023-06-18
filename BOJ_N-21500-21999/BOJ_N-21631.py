def main():
    w, b = map(int, input().split())
    print(b if w >= b else w + 1)


if __name__ == "__main__":
    main()
