def main():
    A, B = map(int, input().split())
    i = 0
    while A != B:
        A, B = max(A, B) - min(A, B), min(A, B)
        i += 1
    print(i)


if __name__ == "__main__":
    main()
