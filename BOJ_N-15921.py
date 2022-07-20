def main():
    N = int(input())
    if N == 0:
        print("divide by zero")
    else:
        p_rec = list(map(int, input().split()))

        count = dict()
        for p in p_rec:
            if p in count:
                count[p] += 1
            else:
                count.update({p: 1})

        avg = sum(p_rec) / N
        exp = sum([i * (count[i] / N) for i in count.keys()])
        if exp == 0:
            print("divide by zero")
        else:
            print("{:0.2f}".format(avg / exp))


if __name__ == "__main__":
    main()
