def main():
    N, S = map(lambda e: int(e) if e.isdigit() else e, input().split())

    ans, chatLog = '', []
    for _ in range(N):
        nickname, chat = input().split()
        if nickname == S:
            ans = chat
        if not ans:
            chatLog.append(chat)
    print(chatLog.count(ans))


if __name__ == "__main__":
    main()
