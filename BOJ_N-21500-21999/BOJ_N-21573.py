def main():
    t_room, t_cond = map(int, input().split())
    mode = input()

    if mode == "freeze":
        print(t_cond if t_room > t_cond else t_room)
    elif mode == "heat":
        print(t_cond if t_room < t_cond else t_room)
    elif mode == "auto":
        print(t_cond)
    elif mode == "fan":
        print(t_room)


if __name__ == "__main__":
    main()
