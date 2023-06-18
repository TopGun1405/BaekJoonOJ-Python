def main():
    temp, mod = 0, []
    while True:
        calc = input()
        op = ['+', '-', '*', '/', '=']
        if calc not in op:
            if not mod:
                temp = int(calc)
            else:
                if mod[0] == '+':
                    temp += int(calc)
                    mod.pop()
                elif mod[0] == '-':
                    temp -= int(calc)
                    mod.pop()
                elif mod[0] == '*':
                    temp *= int(calc)
                    mod.pop()
                elif mod[0] == '/':
                    temp //= int(calc)
                    mod.pop()
        else:
            mod.append(calc)
            if mod[0] == '=':
                print(temp)
                break


if __name__ == "__main__":
    main()
