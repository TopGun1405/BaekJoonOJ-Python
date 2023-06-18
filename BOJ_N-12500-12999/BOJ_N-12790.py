def main():
    T = int(input())
    for _ in range(T):
        HP, MP, ATK, DEF, HP_EQ, MP_EQ, ATK_EQ, DEF_EQ = map(int, input().split())
        HP_TOT = HP + HP_EQ if HP + HP_EQ >= 1 else 1
        MP_TOT = MP + MP_EQ if MP + MP_EQ >= 1 else 1
        ATK_TOT = ATK + ATK_EQ if ATK + ATK_EQ >= 0 else 0
        DEF_TOT = DEF + DEF_EQ
        print(HP_TOT + 5 * MP_TOT + 2 * ATK_TOT + 2 * DEF_TOT)


if __name__ == "__main__":
    main()
