from itertools import combinations


def main():
    height = [int(input()) for _ in range(9)]
    seven = list(filter(lambda e: sum(e) == 100, combinations(height, 7)))
    print(*sorted(seven[0]), sep='\n')


if __name__ == "__main__":
    main()
