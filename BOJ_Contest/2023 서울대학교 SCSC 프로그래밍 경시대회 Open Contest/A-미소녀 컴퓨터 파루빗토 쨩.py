from math import floor


def main():
    formula = input()
    op = list(filter(lambda e: not e[1].isdigit(), enumerate(formula[1:])))[0]
    print(formula[:op[0]+1], formula[op[0]+2:])
    A, B = int(formula[:op[0]+1], 8), int(formula[op[0]+2:], 8)
    op = op[1]
    operators = {'+': lambda a, b: a + b, '-': lambda a, b: a - b,
                 '*': lambda a, b: a * b, '/': lambda a, b: floor(a / b)}
    try:
        print(oct(operators[op](A, B)).replace("0o", ''))
    except ZeroDivisionError:
        print("invalid")


if __name__ == "__main__":
    main()
