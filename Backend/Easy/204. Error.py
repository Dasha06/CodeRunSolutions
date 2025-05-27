def main():
    n = int(input())
    variables = []
    summ = 0
    for i in range(n):
        vari = list(map(int, input().split()))
        variables.append(vari[0]*vari[1])
        summ += variables[i]

    for i in variables:
        print(i / summ)


if __name__ == '__main__':
    main()
