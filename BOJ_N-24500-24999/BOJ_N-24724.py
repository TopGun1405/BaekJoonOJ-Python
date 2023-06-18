def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        A, B = map(int, input().split())
        for _ in range(N):
            u, v = map(int, input().split())
        print("Material Management {}".format(t + 1))
        print("Classification ---- End!")


if __name__ == "__main__":
    main()
