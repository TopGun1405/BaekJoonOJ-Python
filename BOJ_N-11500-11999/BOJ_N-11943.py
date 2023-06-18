def main():
    A, B = map(int, input().split())
    C, D = map(int, input().split())
    print(A + D if A + D < B + C else B + C)


if __name__ == "__main__":
    main()
