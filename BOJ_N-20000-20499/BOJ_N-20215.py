def main():
    w, h = map(int, input().split())
    print(w + h - (w ** 2 + h ** 2) ** 0.5)


if __name__ == "__main__":
    main()
