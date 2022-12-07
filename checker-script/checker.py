import requests
from concurrent.futures import ThreadPoolExecutor
from shodan_parser import ShodanParser

HEADERS = {
    "Authorization": "Basic YWRtaW46d3Jvbmc=",
    "X-Ldap-Realm": "vuln-test281249",
}
filename = 'f093xy11j.json'

lines = []
urls = []
parser = ShodanParser(filename)


def http_get_with_aiohttp(session, url, headers):
    try:
        response = session.get(url=url, headers=headers, timeout=10)
        headers = response.headers
        print(f"Headers = {headers}")
        print(f"Status code = {response.status_code}")
        header = headers['WWW-Authenticate']
        print(header)
        if header.__contains__('vuln'):
            print(f"Find domain {response.url}")
        return response
    except Exception as e:
        print(f"Fail check {url} with {e}")


async def async_check():
    global urls
    session = requests.Session()
    with ThreadPoolExecutor(20) as pool:
        futures = [
            pool.submit(http_get_with_aiohttp, session, url, headers=HEADERS) for url in urls
        ]

        for future in futures:
            if future.cancelled():
                continue
            try:
                if future.result():
                    pool.shutdown(wait=False, cancel_futures=True)
            except ValueError as e:
                print(f"FAIL {e}")


def sync_check():
    session = requests.Session()
    for line in urls:
        try:
            print(f"Start {line}")
            response = session.get(line, headers=HEADERS, timeout=5)
            headers = response.headers
            # print(f"Headers = {headers}")
            print(f"Status code = {response.status_code}")
            header = headers['WWW-Authenticate']
            print(header)
            if header.__contains__('vuln'):
                print(f"Find domain {line}")
                break
        except Exception as e:
            print(f"SKIP {line}")


if __name__ == "__main__":
    parser.parse_file()
    urls = parser.get_urls()
    # asyncio.run(async_check())
    sync_check()
