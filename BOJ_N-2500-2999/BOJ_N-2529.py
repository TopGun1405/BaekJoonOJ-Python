def main():

    def inequality_sign():
        if len(nums) == k + 1:
            for i in range(len(ineq)):
                if ineq[i] == ">" and nums[i] <= nums[i+1]:
                    break
                elif ineq[i] == "<" and nums[i] >= nums[i+1]:
                    break
            else:
                num = "".join(map(str, nums))

                if res['MIN']['NUM'] > int(num):
                    res['MIN']['NUM'] = min(int(num), res['MIN']['NUM'])
                    res['MIN']['STR'] = num

                if res['MAX']['NUM'] < int(num):
                    res['MAX']['NUM'] = max(int(num), res['MAX']['NUM'])
                    res['MAX']['STR'] = num
            return

        for i in range(10):
            if not visited[i]:
                visited[i] = True
                nums.append(i)
                inequality_sign()
                nums.pop()
                visited[i] = False

    k = int(input())
    ineq = input().split()

    nums = []
    visited = [False] * 10
    res = {'MIN': {'NUM': int(1e10), 'STR': ""}, 'MAX': {'NUM': 0, 'STR': ""}}

    inequality_sign()

    print(res['MAX']['STR'])
    print(res['MIN']['STR'])


if __name__ == "__main__":
    main()
