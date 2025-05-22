import sys
from random import sample


def main():
    love_nums = [5, 6, 10]
    n = list(input())
    num_of_operations = int(input())
    res = recursion(num_of_operations, n, love_nums)
    print(res/num_of_operations)


def recursion(num_oper, n, love_nums):
    if num_oper == 1:
        count = 0
        index1, index2 = sample(range(len(n)), 2)
        n[index1], n[index2] = n[index2], n[index1]
        for i in love_nums:
            if int(''.join(n)) % i == 0:
                count += 1
        return count
    else:
        recursion(num_oper - 1, n, love_nums)


if __name__ == '__main__':
    main()
