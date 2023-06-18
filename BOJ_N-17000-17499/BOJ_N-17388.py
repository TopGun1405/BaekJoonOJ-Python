def main():
    name = {0: 'Soongsil', 1: 'Korea', 2: 'Hanyang'}
    skh = list(map(int, input().split()))
    print('OK' if sum(skh) >= 100 else name[skh.index(min(skh))])


if __name__ == "__main__":
    main()
