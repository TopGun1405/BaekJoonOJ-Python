def main():
    height = 0
    for _ in range(4):
        m, x = input().split()
        height = height + int(x) * (21 if m == "Es" else 17)
    print(height)


if __name__ == "__main__":
    main()
