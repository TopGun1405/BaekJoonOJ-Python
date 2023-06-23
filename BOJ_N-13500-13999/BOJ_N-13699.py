def main():
    t = [1]
    for i in range(1, 36):
        ti = 0
        for j in range(i):
            ti += t[j] * t[i-j-1]
        t.append(ti)

    n = int(input())
    print(t[n])


if __name__ == "__main__":
    main()
