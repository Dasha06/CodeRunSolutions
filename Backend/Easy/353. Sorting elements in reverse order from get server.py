from urllib.request import urlopen
import json


def main():
    server = input()
    port = input()
    a = input()
    b = input()

    server_adress = "%s:%s?a=%s&b=%s" % (server, port, a, b)
    data = json.loads(urlopen(server_adress).read())
    print('\n'.join(map(str, filter(lambda x: x > 0, sorted(data, reverse=True)))))


if __name__ == '__main__':
    main()
