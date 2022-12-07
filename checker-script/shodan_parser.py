import json


class ShodanParser:
    def __init__(self, filename):
        self.filename = filename

    def parse_file(self):
        f = open(self.filename)
        lines = f.readlines()
        result = []
        for line in lines:
            data = json.loads(line)
            hosts = data["hostnames"]
            for host in hosts:
                result.append(host + "\n")

        f.close()

        f_out = open('output.txt', 'w')
        for line in result:
            if not str(line).__contains__(".ru"):
                f_out.write(line)

        f_out.close()

    def get_urls(self):
        f_in = open('output.txt')
        lines = f_in.readlines()
        f_in.close()
        if len(lines) == 0:
            self.parse_file()
            f_in = open('output.txt')
            lines = f_in.readlines()
            f_in.close()
        result = []
        for line in lines:
            result.append("https://" + line.replace('\n', ''))
        return result
