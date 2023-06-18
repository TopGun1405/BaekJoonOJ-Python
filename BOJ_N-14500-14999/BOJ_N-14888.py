def main():

    def inputOperator(rec, tot):
        if rec == N:
            result["MAX_VAL"] = max(tot, result["MAX_VAL"])
            result["MIN_VAL"] = min(tot, result["MIN_VAL"])
            return
        for op in ops:
            if ops[op]:
                ops[op] -= 1
                inputOperator(rec + 1, calculator[op](tot, A[rec]))
                ops[op] += 1

    N = int(input())
    A = list(map(int, input().split()))
    ops = {op: v for op, v in zip(['+', '-', '*', '/'], list(map(int, input().split())))}
    calculator = {'+': lambda a, b: a + b, '-': lambda a, b: a - b,
                  '*': lambda a, b: a * b, '/': lambda a, b: int(a / b)}
    result = {"MAX_VAL": -1e9, "MIN_VAL": 1e9}
    inputOperator(1, A[0])
    print(*result.values(), sep='\n')


if __name__ == "__main__":
    main()
