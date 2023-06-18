def main():
    A, B, C, D, E = int(input()), int(input()), int(input()), int(input()), int(input())
    t = 0
    if A < 0:
        t += C * -A
        A = 0
    if A == 0:
        t += D
    t += (B - A) * E
    print(t)


if __name__ == "__main__":
    main()
