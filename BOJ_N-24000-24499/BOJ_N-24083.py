def main():
    A, B = int(input()), int(input())
    t = A + B
    if A + B > 12:
        t = A + B - 12
    print(t % 12 + 12 if t % 12 == 0 else t % 12)


if __name__ == "__main__":
    main()
