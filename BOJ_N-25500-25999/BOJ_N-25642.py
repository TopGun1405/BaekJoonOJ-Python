def main():
    A, B = map(int, input().split())
    while True:
        B += A
        if B >= 5:
            print("yt")
            break
        A += B
        if A >= 5:
            print("yj")
            break


if __name__ == "__main__":
    main()
