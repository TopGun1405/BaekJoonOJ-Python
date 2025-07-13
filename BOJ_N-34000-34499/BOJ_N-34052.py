def main():
    t = [int(input()) for _ in range(4)]
    print("Yes" if 1800 - sum(t) >= 300 else "No")


if __name__ == "__main__":
    main()
