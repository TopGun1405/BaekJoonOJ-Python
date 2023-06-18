def main():
    N = int(input())
    log = [input() for _ in range(N)]
    message = set()
    ans = 0
    for chat in log:
        if chat == "ENTER":
            ans += len(message)
            message.clear()
        else:
            message.add(chat)
    else:
        if log[-1] != "ENTER":
            ans += len(message)
    print(ans)


if __name__ == "__main__":
    main()
