import sys


def main():
    n = int(input())
    a = list(map(int, input().split()))
    nums = {}
    for i in a:
        if i in nums:
            nums[i] += 1
        else:
            nums[i] = 1

    count = 0
    for i in nums:
        if nums[i] == 1:
            count += 1
    print(count)


if __name__ == '__main__':
    main()
