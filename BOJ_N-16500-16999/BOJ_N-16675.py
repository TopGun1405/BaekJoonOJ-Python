def main():
    M_L, M_R, T_L, T_R = input().split()
    if (M_L == "R" or M_R == "R") and (T_L == "S" and T_R == "S"):
        print("MS")
    elif (M_L == "S" or M_R == "S") and (T_L == "P" and T_R == "P"):
        print("MS")
    elif (M_L == "P" or M_R == "P") and (T_L == "R" and T_R == "R"):
        print("MS")
    elif (M_L == "S" and M_R == "S") and (T_L == "R" or T_R == "R"):
        print("TK")
    elif (M_L == "P" and M_R == "P") and (T_L == "S" or T_R == "S"):
        print("TK")
    elif (M_L == "R" and M_R == "R") and (T_L == "P" or T_R == "P"):
        print("TK")
    else:
        print("?")


if __name__ == "__main__":
    main()
