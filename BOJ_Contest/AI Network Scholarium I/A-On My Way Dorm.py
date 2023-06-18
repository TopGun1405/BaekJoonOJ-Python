def main():

    def goBackHome(s, v, commandB):
        s += v
        if s == S:
            for o in op:
                if op[o](v, A[s - 1]) == 0:
                    commandB.append(o)
                    print(''.join(commandB))
                    return
        elif 0 < s < S:
            if s - op['+'](v, A[s - 1]) <= 0:
                commandB.append('0')
                goBackHome(s, op['0'](v, A[s - 1]), commandB)
                commandB.pop()
            else:
                commandB.append('+')
                goBackHome(s, op['+'](v, A[s - 1]), commandB)
                commandB.pop()
        elif S < s < N:
            if s - op['-'](v, A[s - 1]) >= N:
                commandB.append('0')
                goBackHome(s, op['0'](v, A[s - 1]), commandB)
                commandB.pop()
            else:
                commandB.append('-')
                goBackHome(s, op['-'](v, A[s - 1]), commandB)
                commandB.pop()
        print("============================")

    N, S = map(int, input().split())
    A = list(map(int, input().split()))
    command = input().strip()
    op = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '0': lambda a, b: a + 0}
    currV, currS = 0, S
    for c in command:
        currV = op[c](currV, A[currS - 1])
        currS += currV
    goBackHome(currS, currV, [])


if __name__ == "__main__":
    main()
