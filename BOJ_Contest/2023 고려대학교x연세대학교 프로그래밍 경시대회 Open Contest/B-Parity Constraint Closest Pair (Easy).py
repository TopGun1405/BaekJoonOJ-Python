def main():
    N = int(input())
    # O(n**2)
    coord = list(map(int, input().split()))
    diff = []
    for i, x in enumerate(coord[:-1]):
        for y in coord[i+1:]:
            diff.append(abs(x - y))
    even = list(filter(lambda k: k % 2 == 0, diff))
    odd = list(filter(lambda k: k % 2 == 1, diff))
    print((min(even) if even else -1), (min(odd) if odd else -1))
    # ############################################################# #
    coord = sorted(map(int, input().split()))
    even, odd = 1e10, 1e10
    for i, n1 in enumerate(coord[:-1]):
        for n2 in coord[i+1:]:
            if even != 1e10 and odd != 1e10:
                break
            if n1 % 2 == n2 % 2 and n2 - n1 < even:
                even = n2 - n1
            elif n1 % 2 != n2 % 2 and n2 - n1 < odd:
                odd = n2 - n1
        else:
            continue
    print((-1 if even == 1e10 else even), (-1 if odd == 1e10 else odd))


if __name__ == "__main__":
    main()
