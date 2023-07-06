def main():
    k = input()
    nums = {int(kj)-int(ki) for ki, kj in zip(k[:-1], k[1:])}
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!" if len(nums) <= 1 else "흥칫뿡!! <(￣ ﹌ ￣)>")


if __name__ == "__main__":
    main()
