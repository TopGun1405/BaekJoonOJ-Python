def main():
    A, B = map(list, input().split())
    mult = 0
    sA = sum(map(int, A))
    for b in ''.join(B):
        mult += sA * int(b)
    print(mult)


if __name__ == "__main__":
    main()
