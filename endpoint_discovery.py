#!/usr/bin/env python3

import sys
import requests
from colorama import Fore
from optparse import OptionParser


def get_argument():
    parser = OptionParser()
    parser.add_option("-u", "--url", dest="target_url", help="Specify the url for your target website. "
                                                             "Example: --url target.com")
    parser.add_option("-w", "--wordlist", dest="wordlist", help="Specify the wordlist in .txt format to start scanning")
    parser.add_option("-s", "--save", dest="output_file",
                      help="Specify the output file name to save the discovered subdomains (optional)")
    (option, arguments) = parser.parse_args()
    if not option.target_url:
        parser.error("[-] Please specify the target url, or type it correctly, ex: -u target.com")
    elif not option.wordlist:
        parser.error("[-] Please specify a valid wordlist, ex: -w wordlist.txt")
    return option


def make_request(url):
    try:
        return requests.get(url=f"http://{url}")
    except requests.exceptions.InvalidURL:
        pass
    except requests.exceptions.ConnectionError:
        pass


print('')
options = get_argument()

try:
    with open(file=options.wordlist, mode='r') as wordlist_file:
        for line in wordlist_file:
            test_url = f"{options.target_url}/{line.strip()}"
            response = make_request(url=test_url)
            if response:
                print(
                    Fore.GREEN + f"[+] Endpoint Discovered ==> http://{test_url} | Status Code {response.status_code} "
                                 f"| ttl {round(response.elapsed.microseconds * 0.001, 2)} ms")
                if options.output_file:
                    with open(options.output_file, "a") as f:
                        f.writelines(f"{test_url}\n")
            sys.stdout.flush()
        print("")
except KeyboardInterrupt:
    print("\n[*] Detected 'ctrl + c' pressed, program terminated.\n")
