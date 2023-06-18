def main():
    ops = {'>': lambda x, y: x > y, '>=': lambda x, y: x >= y,
           '<': lambda x, y: x < y, '<=': lambda x, y: x <= y,
           '==': lambda x, y: x == y, '!=': lambda x, y: x != y}
    i = 1
    while True:
        a, comp, b = input().split()
        if comp == 'E':
            break
        print(f"Case {i}: {'true' if ops[comp](int(a), int(b)) else 'false'}")
        i += 1


if __name__ == "__main__":
    main()
