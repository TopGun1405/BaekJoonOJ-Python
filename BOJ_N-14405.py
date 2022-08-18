def main():
    S = list(input())
    temp = []
    i = 0
    while i < len(S):
        if i <= len(S) - 2 and S[i] + S[i + 1] == 'pi':
            temp.append(S[i])
            temp.append(S[i + 1])
            i += 2
        elif i <= len(S) - 2 and S[i] + S[i + 1] == 'ka':
            temp.append(S[i])
            temp.append(S[i + 1])
            i += 2
        elif i <= len(S) - 3 and S[i] + S[i + 1] + S[i + 2] == 'chu':
            temp.append(S[i])
            temp.append(S[i + 1])
            temp.append(S[i + 2])
            i += 3
        else:
            i += 1
    print("YES" if len(S) == len(temp) else "NO")


if __name__ == "__main__":
    main()
