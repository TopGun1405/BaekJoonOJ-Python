def main():
    A, B = map(int, input().split())

    tot, res = 9 * 17, 0
    if A == B:
        res = tot - 10 + A
    else:
        score = (A + B) % 10
        for a in range(1, 11):
            for b in range(a+1, 11):
                if score > (a + b) % 10:
                    if a == A and b == B:
                        continue
                    elif a == A or a == B or b == A or b == B:
                        res += 2
                    else:
                        res += 4

    print("{:.3f}".format(res / tot))


if __name__ == "__main__":
    main()
