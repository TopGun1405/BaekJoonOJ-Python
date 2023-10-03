def main():
    N, H = map(int, input().split())
    A = list(map(int, input().split()))
    print(len(list(filter(lambda n: n <= H, A))))


if __name__ == "__main__":
    main()
