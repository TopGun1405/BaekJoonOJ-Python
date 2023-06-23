# def koong(n):
#     if n < 2:
#         return 1
#     elif n == 2:
#         return 2
#     elif n == 3:
#         return 4
#     elif n > 3:
#         return koong(n - 1) + koong(n - 2) + koong(n - 3) + koong(n - 4)


def main():
    t = int(input())

    koong = [1, 1, 2, 4]
    for _ in range(64):
        koong.append(koong[-1] + koong[-2] + koong[-3] + koong[-4])

    for _ in range(t):
        n = int(input())
        print(koong[n])


if __name__ == "__main__":
    main()
