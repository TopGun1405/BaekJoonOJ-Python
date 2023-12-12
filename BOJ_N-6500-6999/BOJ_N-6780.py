def main():
    t1 = int(input())
    t2 = int(input())
    sumac = [t1, t2]
    while True:
        if sumac[-2] < sumac[-1]:
            break
        sumac.append(sumac[-2] - sumac[-1])
    print(len(sumac))


if __name__ == "__main__":
    main()
