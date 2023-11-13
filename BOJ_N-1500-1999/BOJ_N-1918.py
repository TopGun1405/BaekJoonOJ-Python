def main():
    notation = input()

    stack, postfix = [], []
    for token in notation:
        # print(stack, postfix)
        if token.isalpha():
            postfix.append(token)
        else:
            if token == '(':
                stack.append(token)

            elif token in ['*', '/']:
                while stack and stack[-1] in ['*', '/']:
                    postfix.append(stack.pop())
                stack.append(token)

            elif token in ['+', '-']:
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.append(token)

            elif token == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()

    while stack:
        postfix.append(stack.pop())

    print(''.join(postfix))


if __name__ == "__main__":
    main()
