def main():
    a = int(input())
    w, v = map(int, input().split())
    print(1 if a <= w / v else 0)


if __name__ == "__main__":
    main()
