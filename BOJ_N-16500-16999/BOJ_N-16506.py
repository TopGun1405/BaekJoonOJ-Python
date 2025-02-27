def main():
    N = int(input())

    code = {
        'ADD': "00000", 'ADDC': "00001",
        'SUB': "00010", 'SUBC': "00011",
        'MOV': "00100", 'MOVC': "00101",
        'AND': "00110", 'ANDC': "00111",
        'OR': "01000", 'ORC': "01001",
        'NOT': "01010",
        'MULT': "01100", 'MULTC': "01101",
        'LSFTL': "01110", 'LSFTLC': "01111",
        'LSFTR': "10000", 'LSFTRC': "10001",
        'ASFTR': "10010", 'ASFTRC': "10011",
        'RL': "10100", 'RLC': "10101",
        'RR': "10110", 'RRC': "10111"
    }
    resA = {
        'MOV': "000", 'MOVC': "000",
        'NOT': "000"
    }

    for _ in range(N):
        op = input().split()
        if code[op[0]][4] == "0":
            opcode = op[0]
            rD, rA, rB = map(lambda r: format(int(r), "b").zfill(3), op[1:])
            try:
                print(code[opcode] + "0" + rD + resA[opcode] + rB + "0")
            except KeyError:
                print(code[opcode] + "0" + rD + rA + rB + "0")
        else:
            opcode = op[0]
            rD, rA = map(lambda r: format(int(r), "b").zfill(3), op[1:3])
            C = format(int(op[3]), "b").zfill(4)
            try:
                print(code[opcode] + "0" + rD + resA[opcode] + C)
            except KeyError:
                print(code[opcode] + "0" + rD + rA + C)


if __name__ == "__main__":
    main()
