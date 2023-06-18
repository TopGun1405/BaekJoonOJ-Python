def main():
    n = int(input())
    q1, q2, q3, q4, axis = 0, 0, 0, 0, 0
    for _ in range(n):
        x, y = map(int, input().split())
        if x > 0 and y > 0:
            q1 += 1
        elif x < 0 < y:
            q2 += 1
        elif x < 0 and y < 0:
            q3 += 1
        elif x > 0 > y:
            q4 += 1
        else:
            axis += 1
    print("Q1: {}\nQ2: {}\nQ3: {}\nQ4: {}\nAXIS: {}".format(q1, q2, q3, q4, axis))


if __name__ == "__main__":
    main()
