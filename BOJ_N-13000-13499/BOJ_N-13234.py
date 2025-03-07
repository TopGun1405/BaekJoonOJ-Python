def main():
    val1, op, val2 = input().split()

    boole = {'true': 1, 'false': 0, 1: 'true', 0: 'false'}
    operation = {
        'AND': lambda v1, v2: v1 and v2,
        'OR': lambda v1, v2: v1 or v2
    }

    print(boole[operation[op](v1=boole[val1], v2=boole[val2])])


if __name__ == "__main__":
    main()
