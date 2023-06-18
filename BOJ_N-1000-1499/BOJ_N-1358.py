def main():
    W, H, X, Y, P = map(int, input().split())

    count = 0
    for _ in range(P):
        px, py = map(int, input().split())
        if X <= px <= X + W and Y <= py <= Y + H:
            count = count + 1
        elif (X - px) ** 2 + (Y + H / 2 - py) ** 2 <= (H / 2) ** 2:
            count = count + 1
        elif (X + W - px) ** 2 + (Y + H / 2 - py) ** 2 <= (H / 2) ** 2:
            count = count + 1
    print(count)


if __name__ == "__main__":
    main()
