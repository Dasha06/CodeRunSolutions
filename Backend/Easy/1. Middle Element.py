import sys


def main():
    nums = [int(i) for i in input().split(' ')]
    nums.sort()
    print(nums[1])


if __name__ == '__main__':
    main()