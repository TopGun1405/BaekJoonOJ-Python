def main():
    stack = []
    while True:
        S = input()
        if S == "고무오리 디버깅 끝":
            break
        if S == "문제":
            stack.append(1)
        elif S == "고무오리":
            if not stack:
                stack.extend([1, 1])
            else:
                stack.pop()

    print("고무오리야 사랑해" if not stack else "힝구")


if __name__ == "__main__":
    main()
