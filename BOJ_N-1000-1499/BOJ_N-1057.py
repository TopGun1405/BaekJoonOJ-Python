def main():
    N, J, H = map(int, input().split())
    res = 0
    while J != H:
        J, H = J - J//2, H - H//2
        res += 1
    print(res)


if __name__ == "__main__":
    main()
