import sys
import urllib3
import requests
import datetime as dt
from art import directory_art
from argparse import ArgumentParser

if sys.version_info < (3, 0):
    sys.stderr.write("\nYou need python 3.0 or later to run this script\n")
    sys.stderr.write("Please update and make sure you use the command python3 directory_crawler.py -u <url> -w "
                     "<wordlist>\n\n")
    sys.exit(0)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/102.0.0.0 Safari/537.36'}  # It will send the request like browser


def args():
    parser = ArgumentParser()
    parser.add_argument("-u", "--url", dest="target_url", help="Enter URL you want to test. Example: -u "
                                                               "http://example.com/")
    parser.add_argument("-w", "--wordlist", dest="wordlist", help="Choose the wordlist file. Example: -w common.txt")
    options = parser.parse_args()
    if not options.target_url:
        parser.error("[-] Please specify website url, or type it correctly, ex: -u example.com")
    elif not options.wordlist:
        parser.error("[-] Please specify a wordlist file, or type it correctly, ex: -w common.txt")
    return options


def get_details():
    with open(file=args().wordlist, mode='r') as file:
        lines = file.readlines()
    total_line = len(lines)
    print("---------------------")
    print("Start time      : " + str(dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S %p")))
    print("Base URL        : " + args().target_url)
    print("Wordlist file   : " + args().wordlist)
    print("Wordlist counts : " + str(total_line))
    print("---------------------\n")


def request(website_url):
    try:
        return requests.get(url=website_url, headers=HEADERS)
    except requests.exceptions.ConnectionError:
        pass


def main():
    print(directory_art)
    get_details()
    try:
        with open(file=args().wordlist, mode="r") as file:
            for line in file:
                test_url = args().target_url + line.strip()
                # print(test_url)
                response = request(website_url=test_url)
                if response:
                    print(test_url + " | Status Code " + str(response.status_code) + " | TTL " + str(
                        round(response.elapsed.microseconds * 0.001, 2)) + " ms")
                sys.stdout.flush()
    except KeyboardInterrupt:
        print("\n[*] Detected 'ctrl + c' pressed, program terminated.")
        sys.exit(0)


if __name__ == "__main__":
    main()
