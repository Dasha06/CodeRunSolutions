import json


def main():
    n, m = map(int, input().split())
    res = {"offers": []}
    for i in range(n):
        string = input()
        json_data = json.loads(string)
        res["offers"] += json_data["offers"]
    res["offers"] = res["offers"][:m]
    print(json.dumps(res))


if __name__ == '__main__':
    main()
