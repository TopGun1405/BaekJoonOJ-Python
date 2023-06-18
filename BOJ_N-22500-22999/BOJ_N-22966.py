def main():
    N = int(input())
    prob = sorted([input().split() for _ in range(N)], key=lambda k: int(k[1]))
    print(prob[0][0])


if __name__ == "__main__":
    main()
