def main():
    a1, a0 = map(int, input().split())
    c = int(input())
    n0 = int(input())
    print("01"[a1*n0 + a0 <= c*n0 and c - a1 >= 0])


if __name__ == "__main__":
    main()
