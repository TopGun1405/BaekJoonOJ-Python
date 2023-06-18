def main():
    sec = [int(input()) for _ in range(4)]
    print(sum(sec) // 60)
    print(sum(sec) % 60)


if __name__ == "__main__":
    main()
