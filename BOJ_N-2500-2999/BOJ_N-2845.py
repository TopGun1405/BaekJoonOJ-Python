def main():
    L, P = map(int, input().split())
    p_num = map(int, input().split())

    for n in p_num:
        print(n - L * P, end=' ')


if __name__ == "__main__":
    main()
