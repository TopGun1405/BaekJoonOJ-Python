def main():
    s1, s2 = map(int, input().split())
    # print(['H', 'E'][s1 >= s2])
    print('E' if s1 >= s2 / 2 else 'H')


if __name__ == "__main__":
    main()
