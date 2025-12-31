def main():
    A, B, X, Y = map(int, input().split())

    print(min(2 * (max(A, X)+(B + Y)), 2 * ((A + X)+max(B, Y))))


if __name__ == "__main__":
    main()
