from itertools import combinations


def main():
    love_nums = [5, 6, 10]
    n = input().strip()
    num_of_operations = int(input())

    possible_combinations = list(combinations(range(len(n)), 2))
    current_set = set([n])

    for _ in range(num_of_operations):
        next_set = set()
        for num in current_set:
            for pos1, pos2 in possible_combinations:
                if pos1 == pos2:
                    continue
                if num[pos1] == num[pos2]:
                    continue
                new_num = changenum(num, pos1, pos2)
                next_set.add(new_num)
        if not next_set or next_set == current_set:
            break
        current_set = next_set

    count = 0
    for num in current_set:
        int_num = int(num)
        for loveNum in love_nums:
            if int_num % loveNum == 0:
                count += 1
                break

    print(count / len(current_set))


def changenum(n, pos1, pos2):
    if pos1 == pos2:
        return n
    n = list(n)
    n[pos1], n[pos2] = n[pos2], n[pos1]
    return ''.join(n)


if __name__ == '__main__':
    main()
