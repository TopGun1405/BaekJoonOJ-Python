def main():
    P = int(input())
    N = int(input())

    stones = [0] * 100
    for _ in range(N):
        pos, d = map(lambda e: int(e) if e.isdigit() else e, input().split())

        if d == "R":
            for i in range(pos, 100):
                stones[i] += 1
        elif d == "L":
            for i in range(pos-1):
                stones[i] += 1

    R, G, B = 0, 0, 0

    for i in range(100):
        if stones[i] % 3 == 0:
            B += 1
        elif stones[i] % 3 == 1:
            R += 1
        else:
            G += 1

    print(f"{P * B / 100:.02f}\n{P * R / 100:.02f}\n{P * G / 100:.02f}")


if __name__ == "__main__":
    main()
