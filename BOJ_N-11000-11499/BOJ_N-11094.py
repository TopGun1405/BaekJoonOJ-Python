def main():
    N = int(input())
    for _ in range(N):
        command = input()
        if "Simon says" in command:
            print(command.replace("Simon says", "") + " ")
        else:
            pass


if __name__ == "__main__":
    main()
