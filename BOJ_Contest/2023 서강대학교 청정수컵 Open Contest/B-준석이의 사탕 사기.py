def main():
    N = int(input())
    a = list(map(int, input().split()))
    a_odd = sorted(filter(lambda e: e % 2 == 1, a))
    a_even = sorted(filter(lambda e: e % 2 == 0, a))
    print(sum(a_even) + sum(a_odd) - (a_odd[0] if len(a_odd) % 2 else 0))


if __name__ == "__main__":
    main()
