def main():
    N = int(input())
    time = list(map(int, input().split()))
    y, m = 0, 0
    for i in time:
        y += i // 30 * 10 + 10
        m += i // 60 * 15 + 15
    print('Y {}'.format(y) if y < m
          else ('M {}'.format(m) if y > m
                else 'Y M {}'.format(y)))


if __name__ == "__main__":
    main()
