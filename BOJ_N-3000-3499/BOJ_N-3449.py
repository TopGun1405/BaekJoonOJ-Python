def main():
    T = int(input())
    for _ in range(T):
        A, B = input(), input()
        dis = 0
        for a, b in zip(A, B):
            if a != b:
                dis += 1
        print("Hamming distance is {}.".format(dis))


if __name__ == "__main__":
    main()
