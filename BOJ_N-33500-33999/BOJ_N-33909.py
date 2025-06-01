def main():
    b_S, b_C, b_O, b_N = map(int, input().split())

    b_C += b_O * 2
    b_S += b_N

    print(min(b_C // 6, b_S // 3))


if __name__ == "__main__":
    main()
