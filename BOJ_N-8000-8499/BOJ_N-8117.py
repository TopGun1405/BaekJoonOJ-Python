def main():
    lines = []
    while True:
        n = int(input())
        if n == 0:
            break
        lines.append(n)
    lines.sort(reverse=True)

    for i, l1 in enumerate(lines):
        for j, l2 in enumerate(lines[i+1:]):
            for l3 in lines[i+j+2:]:
                if l1 < l2 + l3:
                    print(l1, l2, l3)
                    exit(0)
    else:
        print("NIE")


if __name__ == "__main__":
    main()
