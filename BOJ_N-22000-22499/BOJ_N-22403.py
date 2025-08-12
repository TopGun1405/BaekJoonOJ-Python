def main():
    N = int(input())
    S = [input() for _ in range(N)]

    stack = []
    for S_i in S:
        if S_i == "A":
            stack.append(S_i)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        print("YES" if not stack else "NO")


if __name__ == "__main__":
    main()
