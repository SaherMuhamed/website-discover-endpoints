import sys
import queue
import urllib3
import requests
import threading
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
THREADS = 50


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


def print_details():
    with open(file=args().wordlist, mode='r') as file:
        lines = file.readlines()
    total_line = len(lines)
    print("---------------------")
    print("🕰️  Start Time  : " + str(dt.datetime.now().strftime("%d/%m/%Y %I:%M %p")))
    print("🎯 Target URL  : " + args().target_url)
    print("🚀 Threads     : " + str(THREADS))
    print("📖 Wordlist    : " + args().wordlist)
    print("🔢 No. Words   : " + str(total_line))
    print("---------------------")


def fetch_wordlist_file():
    with open(file=args().wordlist, mode="r") as f:
        raw_words = f.read()
    queued_words = queue.Queue()
    for word in raw_words.split():
        queued_words.put(item=word)
    return queued_words


def make_request(website_url):
    try:
        return requests.get(url=website_url, headers=HEADERS)
    except requests.exceptions.ConnectionError:
        sys.stderr.write("x")
        sys.stderr.flush()


def main(word):
    while not word.empty():
        url = f"{args().target_url}{word.get()}"
        r = make_request(website_url=url)
        try:
            if r.status_code == 200:
                print(f"\nSuccess ({r.status_code}: {url})")
            elif r.status_code == 404:
                sys.stderr.write(".")
                sys.stderr.flush()
            else:
                print(f"\n{r.status_code} => {url}")
        except AttributeError:
            pass
            continue


if __name__ == "__main__":
    print(directory_art)
    print_details()
    words = fetch_wordlist_file()
    for _ in range(THREADS):
        t = threading.Thread(target=main, args=(words,))
        t.start()
