def main():
    pad = {'1': "", '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
           '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

    nums = input().split()
    pad_ = {str(i+1): pad[nums[i]] for i in range(len(nums))}
    s = input()

    res, key = "", []
    for i in range(len(s)):
        for k, v in pad_.items():
            if s[i] in v:
                if len(key) > 0 and key[-1] == k:
                    res += "#" + (v.find(s[i]) + 1) * k
                else:
                    res += (v.find(s[i]) + 1) * k
                key.append(k)

    print(res)


if __name__ == "__main__":
    main()
