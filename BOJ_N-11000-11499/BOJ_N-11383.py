def main():
    N, M = map(int, input().split())
    image1 = [''.join(map(lambda c: c * 2, input())) for _ in range(N)]
    image2 = [input() for _ in range(N)]
    for i in range(N):
        if image1[i] != image2[i]:
            print("Not Eyfa")
            break
    else:
        print("Eyfa")


if __name__ == "__main__":
    main()
