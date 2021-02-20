#!/usr/bin/env python3

import os, requests, time, sys, threading
from bs4 import BeautifulSoup
from colorama import Fore

message = 'GitCheck by Wrath/Shinigami\n'

def proxys(): # grab proxies
    try:
        r = requests.get("https://sslproxies.org/")
        s = BeautifulSoup(r.content, 'html5lib')
        proxy = {'https': choice(list(map(lambda x:x[0]+':'+x[1], list(zip(map(lambda x:x.text,
        soup.findAll('td')[::8]), map(lambda x:x.text, soup.findAll('td')[1::8]))))))}
        return proxy
    except Exception as e:
        pass

def banner(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)


def main():
    banner(message)
    if len(sys.argv) < 1:
        print("Usage: python3 gitcheck.py <list>")
        sys.exit()
    elif len(sys.argv[1]):
        ulist = sys.argv[1]
        proxy = proxys()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
        try:
            with open(f"{ulist}") as f:
                content = f.readlines()
            content = [x.strip() for x in content]
            for username in content:
                res = requests.get("https://github.com/" + username, headers=headers, proxies=proxy)
                if res.status_code == 404:
                    print(f"[{Fore.GREEN}+{Fore.WHITE}] : {username} is available!")
                elif res.status_code == 200:
                    print(f"[{Fore.RED}-{Fore.WHITE}] : {username} is taken!")
                else:
                    print("Unknown Status Code.")
        except Exception as e:
            print(e)

main()
