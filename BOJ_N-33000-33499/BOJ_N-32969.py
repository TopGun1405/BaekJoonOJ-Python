def main():
    s = input().lower()

    for s_i in ["social", "history", "language", "literacy"]:
        if s.find(s_i) != -1:
            print("digital humanities")
            break
    else:
        for s_i in ["bigdata", "public", "society"]:
            if s.find(s_i) != -1:
                print("public bigdata")
                break


if __name__ == "__main__":
    main()
