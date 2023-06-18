def main():
    num13 = [9, 7, 8, 0, 9, 2, 1, 4, 1, 8]
    for _ in range(3):
        num13.append(int(input()))
    for i in range(13):
        if i % 2 == 0:
            num13[i] *= 1
        else:
            num13[i] *= 3
    print("The 1-3-sum is {}".format(sum(num13)))


if __name__ == "__main__":
    main()
